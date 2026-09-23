# Full-Stack Observability: Metrics, Tracing & Logging — lesson m03l05 — Dashboards That Answer Questions
# https://learnsome.tech/courses/observability-course/watch?lesson=m03l05
# © LearnSome.tech
"""One second of real latencies. The average is fine, the service is not."""

LATENCIES_MS = ([40] * 90) + ([60] * 6) + [820, 910, 1500, 2400]

ordered = sorted(LATENCIES_MS)


def quantile(values, q):
    """Nearest rank: the smallest value at or above the qth fraction."""
    return values[max(1, round(q * len(values))) - 1]


print("requests:", len(ordered))
print("mean ms:", round(sum(ordered) / len(ordered), 1))
print("median ms:", quantile(ordered, 0.5))
print("p90 ms:", quantile(ordered, 0.9))
print("p99 ms:", quantile(ordered, 0.99))
print("slower than one second:", sum(1 for v in ordered if v > 1000))
