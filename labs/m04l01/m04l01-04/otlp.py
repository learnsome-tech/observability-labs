# Full-Stack Observability: Metrics, Tracing & Logging — lesson m04l01 — OpenTelemetry: The Vendor Neutral Path
# https://learnsome.tech/courses/observability-course/watch?lesson=m04l01
# © LearnSome.tech
def attribute(key, value):
    """Attributes are typed in OTLP: a string is not an integer."""
    if isinstance(value, bool):
        return {"key": key, "value": {"boolValue": value}}
    if isinstance(value, int):
        return {"key": key, "value": {"intValue": str(value)}}
    if isinstance(value, float):
        return {"key": key, "value": {"doubleValue": value}}
    return {"key": key, "value": {"stringValue": str(value)}}
