import otlp

LEVELS = {"DEBUG": 10, "INFO": 20, "WARN": 30, "ERROR": 40}
SEVERITY = {"DEBUG": 5, "INFO": 9, "WARN": 13, "ERROR": 17}
THRESHOLD = LEVELS.get(os.environ.get("LOG_LEVEL", "INFO").upper(), 20)
SERVICE = os.environ.get("SERVICE_NAME", "checkout")


def log(level, event, **fields):
    """Write one JSON record, or nothing when the level is filtered out."""
    if LEVELS.get(level, 20) < THRESHOLD:
        return
