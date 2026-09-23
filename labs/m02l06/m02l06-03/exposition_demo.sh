#!/usr/bin/env bash
# Full-Stack Observability: Metrics, Tracing & Logging — lesson m02l06 — The Prometheus Exposition Format
# https://learnsome.tech/courses/observability-course/watch?lesson=m02l06
# © LearnSome.tech
# What a Prometheus scrape actually fetches: one text page, no protocol.
#
# Three requests to a route that does no work, so the numbers below are
# the same every time you run this.
set -euo pipefail
cd "$(dirname "$0")"

PORT=8002 python3 app.py > /dev/null 2>&1 &
sleep 1
for _ in 1 2 3; do curl -s http://localhost:8002/healthz > /dev/null; done
curl -s http://localhost:8002/metrics | grep -v duration_seconds
kill %1
