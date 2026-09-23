# Full-Stack Observability: Metrics, Tracing & Logging — lesson m03l01 — PromQL Basics And Selectors
# https://learnsome.tech/courses/observability-course/watch?lesson=m03l01
# © LearnSome.tech
"""Cardinality is a multiplication nobody does before shipping."""

LABELS = [("method", 4), ("route", 20), ("status", 6), ("instance", 12)]
BYTES_PER_SERIES = 3200


def report(labels):
    """Every combination of label values is one more time series."""
    series = 1
    for _, count in labels:
        series *= count
    print("labels:", [name for name, _ in labels])
    print("series:", series)
    print("memory mb:", round(series * BYTES_PER_SERIES / 1_000_000, 1))


report(LABELS)
print("---")
report(LABELS + [("user_id", 50_000)])
