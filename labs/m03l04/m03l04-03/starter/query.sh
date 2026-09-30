#!/usr/bin/env bash
# Ask Prometheus a question from the shell and print just the answer.
#
# usage: ./query.sh 'sum(rate(demo_http_requests_total[5m]))' [when]
#
# The default time is the middle of the recorded hour this course ships,
# so every answer in these lessons is the answer you get too. Pass the
# word now to ask about the service running on this machine instead.
set -euo pipefail

query=${1:?usage: query.sh EXPRESSION [when]}
at=${2:-1773482400}
if [ "$at" = now ]; then at=$(date +%s); fi

curl -sG --data-urlencode "query=$query" --data-urlencode "time=$at" \
  http://localhost:9090/api/v1/query |
  jq -r '.data.result[] | "\(.metric | tostring) \(.value[1])"' | sort
