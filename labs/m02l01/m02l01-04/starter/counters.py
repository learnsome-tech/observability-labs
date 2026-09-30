"""A counter means nothing until you ask it a question about time."""

SAMPLES = [(0, 100), (15, 130), (30, 160), (45, 5), (60, 35)]


def increase(samples):
    """Sum the steps, treating a fall as a restart, exactly as rate does."""
    total = 0.0
    for (_, before), (_, after) in zip(samples, samples[1:]):
        total += after - before if after >= before else after
    return total


span = SAMPLES[-1][0] - SAMPLES[0][0]
print("raw difference:", SAMPLES[-1][1] - SAMPLES[0][1])
print("increase with reset handling:", increase(SAMPLES))
print("seconds:", span)
print("per second:", round(increase(SAMPLES) / span, 4))
