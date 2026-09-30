# m02l02-03 · What a histogram looks like on the wire

**Lesson:** [Metric Types: Summaries And Histograms](https://learnsome.tech/learn/observability-course/m02l02) (lesson 2.2, module 2: Metrics And Prometheus) · Pro  
**Check:** Graded

## Goal

You can explain how a histogram stores a distribution in counters, why a summary cannot be aggregated across instances, and how to choose bucket boundaries.

In the lesson: Now see it from the outside. This registers a counter and a histogram with four boundaries, observes five durations, and prints the page. Read the bucket lines in order. Two observations were under fifty milliseconds, three under a hundred, four under half a second, still four under one second, and five in the bucket labelled plus infinity, which always equals the total count. The counts never go down as the boundary grows, because each bucket includes everything below it. Underneath, each of those lines is an ordinary counter, with a label called l e carrying the upper bound. There is no special protocol for a distribution. There is a naming convention and some discipline.

## Files

- [`starter/exposition.py`](starter/exposition.py): the listing from the lesson
- [`starter/metrics.py`](starter/metrics.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-03/starter`
2. Read `exposition.py`.
3. Run it: `python3 exposition.py`.
4. Check it from the repository root: `./check m02l02-03`.

## Expected output

```text
# HELP http_requests_total Requests handled.
# TYPE http_requests_total counter
http_requests_total{status="200"} 5
http_requests_total{status="500"} 1
# HELP http_request_duration_seconds Duration in seconds.
# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{le="0.05"} 2
http_request_duration_seconds_bucket{le="0.1"} 3
http_request_duration_seconds_bucket{le="0.5"} 4
http_request_duration_seconds_bucket{le="1"} 4
http_request_duration_seconds_bucket{le="+Inf"} 5
http_request_duration_seconds_sum 2.471
http_request_duration_seconds_count 5
```

## How to check

`./check m02l02-03` copies `starter/` into a scratch directory and runs `python3 exposition.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
