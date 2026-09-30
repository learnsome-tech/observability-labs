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
