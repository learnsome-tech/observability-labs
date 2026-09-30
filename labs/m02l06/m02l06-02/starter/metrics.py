"""The metric types Prometheus understands, in about a hundred lines.

A real service would import prometheus_client. This module exists so the
course can show every moving part: how a counter differs from a gauge, how
a histogram stores buckets, and what the scrape endpoint actually returns.
"""


def _labels(names, values):
    """Render a label set the way the exposition format writes it."""
    if not names:
        return ""
    pairs = ",".join(f'{n}="{v}"' for n, v in zip(names, values))
    return "{" + pairs + "}"


class Counter:
    """A value that only ever goes up, or resets to zero on restart."""

    kind = "counter"

    def __init__(self, name, help_text, labels=()):
        self.name = name
        self.help_text = help_text
        self.labels = tuple(labels)
        self.values = {}

    def inc(self, amount=1.0, **labels):
        key = tuple(str(labels.get(n, "")) for n in self.labels)
        self.values[key] = self.values.get(key, 0.0) + amount

    def samples(self):
        for key in sorted(self.values):
            yield self.name + _labels(self.labels, key), self.values[key]


class Gauge:
    """A value that goes up and down: queue depth, temperature, memory."""

    kind = "gauge"

    def __init__(self, name, help_text, labels=()):
        self.name = name
        self.help_text = help_text
        self.labels = tuple(labels)
        self.values = {}

    def set(self, value, **labels):
        self.values[tuple(str(labels.get(n, "")) for n in self.labels)] = value

    def add(self, delta, **labels):
        key = tuple(str(labels.get(n, "")) for n in self.labels)
        self.values[key] = self.values.get(key, 0.0) + delta

    def samples(self):
        for key in sorted(self.values):
            yield self.name + _labels(self.labels, key), self.values[key]


class Histogram:
    """Counts observations into cumulative buckets, plus a sum and a count.

    Every bucket holds the number of observations less than or equal to its
    upper bound, which is why the last bucket, plus infinity, equals count.
    """

    kind = "histogram"
    DEFAULT = (0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0)

    def __init__(self, name, help_text, labels=(), buckets=DEFAULT):
        self.name = name
        self.help_text = help_text
        self.labels = tuple(labels)
        self.buckets = tuple(sorted(buckets))
        self.counts = {}
        self.sums = {}
        self.totals = {}

    def observe(self, value, **labels):
        key = tuple(str(labels.get(n, "")) for n in self.labels)
        counts = self.counts.setdefault(key, [0] * len(self.buckets))
        for i, bound in enumerate(self.buckets):
            if value <= bound:
                counts[i] += 1
        self.sums[key] = self.sums.get(key, 0.0) + value
        self.totals[key] = self.totals.get(key, 0) + 1

    def samples(self):
        for key in sorted(self.counts):
            names = self.labels + ("le",)
            for bound, count in zip(self.buckets, self.counts[key]):
                bucket = _labels(names, key + (_num(bound),))
                yield f"{self.name}_bucket{bucket}", count
            infinity = _labels(names, key + ("+Inf",))
            yield f"{self.name}_bucket{infinity}", self.totals[key]
            tail = _labels(self.labels, key)
            yield f"{self.name}_sum{tail}", self.sums[key]
            yield f"{self.name}_count{tail}", self.totals[key]


def _num(value):
    """Bucket bounds print as Go prints them: 1 rather than 1.0."""
    text = repr(float(value))
    return text[:-2] if text.endswith(".0") else text


class Registry:
    """Holds the metrics and renders the page a Prometheus scrape reads."""

    def __init__(self):
        self.metrics = []

    def register(self, metric):
        self.metrics.append(metric)
        return metric

    def render(self):
        lines = []
        for metric in self.metrics:
            lines.append(f"# HELP {metric.name} {metric.help_text}")
            lines.append(f"# TYPE {metric.name} {metric.kind}")
            for series, value in metric.samples():
                lines.append(f"{series} {_num(value)}")
        return "\n".join(lines) + "\n"
