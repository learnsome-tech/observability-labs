"""The arithmetic Prometheus does to turn counted buckets into a percentile."""

BUCKETS = [(0.05, 90), (0.1, 96), (0.25, 96), (0.5, 96), (1.0, 97),
           (2.5, 100), (float("inf"), 100)]


def histogram_quantile(q, buckets):
    """Find the bucket holding the rank, then interpolate inside it."""
    target = q * buckets[-1][1]
    lower, lower_count = 0.0, 0
    for bound, count in buckets:
        if count >= target:
            if bound == float("inf"):
                return lower
            share = (target - lower_count) / (count - lower_count)
            return lower + (bound - lower) * share
        lower, lower_count = bound, count
    return lower


for q in (0.5, 0.9, 0.95, 0.99):
    print(f"p{int(q * 100)}", round(histogram_quantile(q, BUCKETS), 4))
