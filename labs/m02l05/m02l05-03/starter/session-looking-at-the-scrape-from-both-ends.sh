#!/usr/bin/env bash
# Terminal session from the video, as a file you can run.
# Each uncommented line was typed at the prompt; the commented lines
# below it are what the machine answered. Run it with:  bash thisfile.sh
set -euo pipefail

cd stack
docker compose ps --format '{{.Service}} {{.Status}}' | sort
#   grafana Up 16 minutes
#   loki Up 16 minutes
#   otel-collector Up 16 minutes
#   prometheus Up 16 minutes
#   service Up 5 minutes
curl -s localhost:9090/api/v1/targets | jq -r '.data.activeTar
#   http://localhost:9090/metrics
#   http://otel-collector:8888/metrics
#   http://service:8000/metrics
curl -s 'localhost:9090/api/v1/query?query=up' | jq -r '.data.
#   checkout 1
#   otel-collector 1
#   prometheus 1
curl -s -o /dev/null -w '%{http_code}\n' localhost:8000/metric
#   200
