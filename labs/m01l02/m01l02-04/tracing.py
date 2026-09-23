# Full-Stack Observability: Metrics, Tracing & Logging — lesson m01l02 — The Three Signals: Logs, Metrics And Traces
# https://learnsome.tech/courses/observability-course/watch?lesson=m01l02
# © LearnSome.tech
"""A tracer small enough to read: spans, ids, and the traceparent header.

A span is one unit of work with a start, an end and a parent. A trace is
the tree of spans that share a trace id. Context propagation is what
carries that id from one service to the next, over a header.
"""

import random
import time

import otlp


def new_trace_id():
    return f"{random.getrandbits(128):032x}"


def new_span_id():
    return f"{random.getrandbits(64):016x}"


def format_traceparent(trace_id, span_id, sampled=True):
    """W3C trace context: version, trace id, parent span id, then flags."""
    return f"00-{trace_id}-{span_id}-{'01' if sampled else '00'}"


def parse_traceparent(header):
    """Return the trace id and span id of an incoming request, or None."""
    parts = (header or "").split("-")
    if len(parts) != 4 or parts[0] != "00":
        return None
    if len(parts[1]) != 32 or len(parts[2]) != 16:
        return None
    return parts[1], parts[2]


class Span:
    def __init__(self, name, trace_id, span_id, parent_id=None):
        self.name = name
        self.trace_id = trace_id
        self.span_id = span_id
        self.parent_id = parent_id
        self.start_ns = time.time_ns()
        self.end_ns = None
        self.attributes = {}
        self.status = "OK"

    def set(self, key, value):
        self.attributes[key] = value
        return self

    def child(self, name):
        return Span(name, self.trace_id, new_span_id(), self.span_id)

    def end(self, status="OK"):
        self.status = status
        self.end_ns = time.time_ns()
        return self


def to_otlp(spans):
    """Wrap finished spans in the envelope a collector accepts."""
    return {"resourceSpans": [{
        "resource": otlp.resource(),
        "scopeSpans": [{
            "scope": {"name": "course.tracer"},
            "spans": [{
                "traceId": s.trace_id,
                "spanId": s.span_id,
                "parentSpanId": s.parent_id or "",
                "name": s.name,
                "kind": 2,
                "startTimeUnixNano": str(s.start_ns),
                "endTimeUnixNano": str(s.end_ns or s.start_ns),
                "attributes": [otlp.attribute(k, v)
                               for k, v in sorted(s.attributes.items())],
                "status": {"code": 2 if s.status == "ERROR" else 1},
            } for s in spans],
        }],
    }]}


def export(spans, endpoint=None):
    if not spans:
        return False
    return otlp.post("/v1/traces", to_otlp(spans), endpoint)
