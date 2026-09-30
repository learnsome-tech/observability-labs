"""The same event stream, counted two ways. Only one of them can go down."""

import sys

sys.path.insert(0, "../service")
from metrics import Counter, Gauge

ARRIVALS = [3, 5, 0, 4, 2]
DEPARTURES = [1, 2, 4, 3, 2]

jobs_total = Counter("jobs_enqueued_total", "Jobs ever enqueued.")
queue_depth = Gauge("queue_depth", "Jobs waiting right now.")

for arrived, left in zip(ARRIVALS, DEPARTURES):
    jobs_total.inc(arrived)
    queue_depth.add(arrived - left)
    total = dict(jobs_total.samples())["jobs_enqueued_total"]
    depth = dict(queue_depth.samples())["queue_depth"]
    print(f"enqueued so far {total:5}   waiting now {depth:5}")
