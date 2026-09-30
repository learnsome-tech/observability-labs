"""Why records beat prose: the question is code, not a regex.

Both files hold the same three events. Only one of them can answer
how much money the accepted orders were worth.
"""

import json

orders = [json.loads(line) for line in open("orders.jsonl")]
big = [o for o in orders if o["total_gbp"] > 50]
print("events:", len(orders))
print("over fifty pounds:", len(big))
print("total:", round(sum(o["total_gbp"] for o in orders), 2))
print("by user:", sorted({o["user_id"] for o in orders}))
