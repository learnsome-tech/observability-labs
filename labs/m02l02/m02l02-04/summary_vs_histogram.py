# Full-Stack Observability: Metrics, Tracing & Logging — lesson m02l02 — Metric Types: Summaries And Histograms
# https://learnsome.tech/courses/observability-course/watch?lesson=m02l02
# © LearnSome.tech
"""Why a summary cannot be aggregated, and a histogram can."""

A = [0.02] * 90 + [0.3] * 9 + [2.0]
B = [0.02] * 50 + [0.9] * 49 + [4.0]
BOUNDS = [0.05, 0.5, 1.0, 2.5]


def rank(values, q):
    return sorted(values)[max(1, round(q * len(values))) - 1]


def buckets(values):
    return [sum(1 for v in values if v <= b) for b in BOUNDS] + [len(values)]


print("instance a, ninety ninth:", rank(A, 0.99))
print("instance b, ninety ninth:", rank(B, 0.99))
print("mean of those two:", (rank(A, 0.99) + rank(B, 0.99)) / 2)
print("true ninety ninth of both:", rank(A + B, 0.99))
print("buckets a:", buckets(A))
print("buckets b:", buckets(B))
