# Full-Stack Observability: Metrics, Tracing & Logging — lesson m05l03 — Service Level Indicators
# https://learnsome.tech/courses/observability-course/watch?lesson=m05l03
# © LearnSome.tech
if __name__ == "__main__":
    conf = load()
    print("service:", conf["service"])
    print("objective:", conf["objective"])
    print("window days:", conf["window_days"])
    print("error budget:", round(1 - conf["objective"], 4))
