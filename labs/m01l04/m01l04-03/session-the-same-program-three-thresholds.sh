#!/usr/bin/env bash
# Full-Stack Observability: Metrics, Tracing & Logging — lesson m01l04 — Log Levels Done Properly
# https://learnsome.tech/courses/observability-course/watch?lesson=m01l04
# © LearnSome.tech
# Terminal session from the video, as a file you can run.
# Each uncommented line was typed at the prompt; the commented lines
# below it are what the machine answered. Run it with:  bash thisfile.sh
set -euo pipefail

cd logs
python3 levels.py
#   {"ts": "2026-09-11T09:55:22Z", "level": "INFO", "service": "checkout", "event": "order_accepted", "order_id": 1071}
#   {"ts": "2026-09-11T09:55:22Z", "level": "WARN", "service": "checkout", "event": "retry_succeeded", "attempt": 2}
#   {"ts": "2026-09-11T09:55:22Z", "level": "ERROR", "service": "checkout", "event": "order_rejected", "reason": "timeout"}
LOG_LEVEL=DEBUG python3 levels.py
#   {"ts": "2026-09-11T09:55:22Z", "level": "DEBUG", "service": "checkout", "event": "cache_lookup", "key": "user:42"}
#   {"ts": "2026-09-11T09:55:22Z", "level": "INFO", "service": "checkout", "event": "order_accepted", "order_id": 1071}
#   {"ts": "2026-09-11T09:55:22Z", "level": "WARN", "service": "checkout", "event": "retry_succeeded", "attempt": 2}
#   {"ts": "2026-09-11T09:55:22Z", "level": "ERROR", "service": "checkout", "event": "order_rejected", "reason": "timeout"}
LOG_LEVEL=ERROR python3 levels.py
#   {"ts": "2026-09-11T09:55:22Z", "level": "ERROR", "service": "checkout", "event": "order_rejected", "reason": "timeout"}
