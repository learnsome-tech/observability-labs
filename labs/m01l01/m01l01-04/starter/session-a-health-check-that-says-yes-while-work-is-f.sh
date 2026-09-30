#!/usr/bin/env bash
# Terminal session from the video, as a file you can run.
# Each uncommented line was typed at the prompt; the commented lines
# below it are what the machine answered. Run it with:  bash thisfile.sh
set -euo pipefail

curl -s localhost:8000/healthz
#   {"status": "ok"}
curl -s localhost:8000/nope
#   {"error": "no such route"}
curl -s localhost:8000/metrics | grep 404 | cut -d' ' -f1
#   http_requests_total{method="GET",route="/nope",status="404"}
