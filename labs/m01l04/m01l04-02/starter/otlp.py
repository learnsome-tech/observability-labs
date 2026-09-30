"""One exporter, shared by every signal the service emits.

OTLP over HTTP with a JSON body is part of the specification, so a
service can speak it with nothing but the standard library, and the
collector on the other end cannot tell the difference.
"""

import json
import os
import urllib.error
import urllib.request

ENDPOINT = os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT", "")
SERVICE = os.environ.get("SERVICE_NAME", "checkout")
TIMEOUT = 2


def attribute(key, value):
    """Attributes are typed in OTLP: a string is not an integer."""
    if isinstance(value, bool):
        return {"key": key, "value": {"boolValue": value}}
    if isinstance(value, int):
        return {"key": key, "value": {"intValue": str(value)}}
    if isinstance(value, float):
        return {"key": key, "value": {"doubleValue": value}}
    return {"key": key, "value": {"stringValue": str(value)}}


def resource():
    return {"attributes": [attribute("service.name", SERVICE)]}


def post(path, payload, endpoint=None):
    """Send one payload. Telemetry must never break the request it traces."""
    target = endpoint if endpoint is not None else ENDPOINT
    if not target:
        return False
    request = urllib.request.Request(
        target.rstrip("/") + path, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return response.status < 300
    except (urllib.error.URLError, OSError):
        return False
