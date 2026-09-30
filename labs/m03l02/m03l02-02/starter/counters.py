span = SAMPLES[-1][0] - SAMPLES[0][0]
print("raw difference:", SAMPLES[-1][1] - SAMPLES[0][1])
print("increase with reset handling:", increase(SAMPLES))
print("seconds:", span)
print("per second:", round(increase(SAMPLES) / span, 4))
