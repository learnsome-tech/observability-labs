# Full-Stack Observability: Metrics, Tracing & Logging — lesson m01l02 — The Three Signals: Logs, Metrics And Traces
# https://learnsome.tech/courses/observability-course/watch?lesson=m01l02
# © LearnSome.tech
"""The same three events as records: one JSON object per line."""

import json

ORDERS = [(1071, 31.86, "u4"), (1072, 74.63, "u1"), (1073, 8.5, "u4")]

for order, total, user in ORDERS:
    print(json.dumps({"event": "order_accepted", "order_id": order,
                      "total_gbp": total, "user_id": user}))
