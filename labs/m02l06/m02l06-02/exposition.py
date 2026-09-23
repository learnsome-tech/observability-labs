# Full-Stack Observability: Metrics, Tracing & Logging — lesson m02l06 — The Prometheus Exposition Format
# https://learnsome.tech/courses/observability-course/watch?lesson=m02l06
# © LearnSome.tech
"""The page a Prometheus scrape fetches, built from known observations."""

import sys

sys.path.insert(0, "../service")
from metrics import Counter, Histogram, Registry
registry = Registry()
requests = registry.register(
    Counter("http_requests_total", "Requests handled.", ("status",)))
latency = registry.register(
    Histogram("http_request_duration_seconds", "Duration in seconds.",
              buckets=(0.05, 0.1, 0.5, 1.0)))
for seconds in (0.031, 0.042, 0.088, 0.41, 1.9):
    requests.inc(status=200)
    latency.observe(seconds)
requests.inc(status=500)
print(registry.render(), end="")
