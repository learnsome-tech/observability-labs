# Full-Stack Observability: Metrics, Tracing & Logging — lesson m03l02 — Rates And Increases Over Time
# https://learnsome.tech/courses/observability-course/watch?lesson=m03l02
# © LearnSome.tech
span = SAMPLES[-1][0] - SAMPLES[0][0]
print("raw difference:", SAMPLES[-1][1] - SAMPLES[0][1])
print("increase with reset handling:", increase(SAMPLES))
print("seconds:", span)
print("per second:", round(increase(SAMPLES) / span, 4))
