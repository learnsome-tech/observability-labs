#!/usr/bin/env bash
# Start the service, send it a known amount of traffic, scrape it once.
#
# Everything here is deterministic: the same twenty requests in the same
# order, so the same counters come back from the metrics page every time.
set -euo pipefail
cd "$(dirname "$0")"

SEED=7 FAIL_RATE=0 PORT=8001 python3 app.py > /dev/null 2>&1 &
sleep 1
python3 loadgen.py 20 http://localhost:8001 > /dev/null
curl -s http://localhost:8001/metrics | grep http_requests_total
kill %1
