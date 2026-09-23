# Full-Stack Observability: Metrics, Tracing & Logging — lesson m01l03 — Structured Logging And Why Text Fails
# https://learnsome.tech/courses/observability-course/watch?lesson=m01l03
# © LearnSome.tech
LEVELS = {"DEBUG": 10, "INFO": 20, "WARN": 30, "ERROR": 40}
SEVERITY = {"DEBUG": 5, "INFO": 9, "WARN": 13, "ERROR": 17}
THRESHOLD = LEVELS.get(os.environ.get("LOG_LEVEL", "INFO").upper(), 20)
SERVICE = os.environ.get("SERVICE_NAME", "checkout")


def log(level, event, **fields):
    """Write one JSON record, or nothing when the level is filtered out."""
    if LEVELS.get(level, 20) < THRESHOLD:
        return
    record = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "level": level, "service": SERVICE, "event": event}
    record.update(fields)
    sys.stdout.write(json.dumps(record) + "\n")
    sys.stdout.flush()
    otlp.post("/v1/logs", to_otlp(record))
