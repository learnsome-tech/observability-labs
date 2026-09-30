"""A trace is a tree of spans sharing one id, and a header carries it."""

import random

import tracing

random.seed(3)
root = tracing.Span("GET /checkout", tracing.new_trace_id(),
                    tracing.new_span_id())
db = root.child("SELECT basket")
db.set("db.system", "postgresql").end()
pay = root.child("POST payments")
pay.set("http.response.status_code", 500).end("ERROR")
root.end("ERROR")
for span in (root, db, pay):
    print(f"{span.name:<16} span={span.span_id} "
          f"parent={span.parent_id or 'none'}")
header = tracing.format_traceparent(root.trace_id, pay.span_id)
print("traceparent:", header)
print("downstream reads:", tracing.parse_traceparent(header)[0])
print("same trace:", tracing.parse_traceparent(header)[0] == root.trace_id)
