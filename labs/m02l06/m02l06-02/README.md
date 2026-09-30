# m02l06-02 · A page, rendered from known observations

**Lesson:** [The Prometheus Exposition Format](https://learnsome.tech/learn/observability-course/m02l06) (lesson 2.6, module 2: Metrics And Prometheus) · Pro  
**Check:** Graded

## Goal

You can read and write the text format a scrape returns, including help and type lines, label syntax, histogram buckets, and the rules that make a page valid.

In the lesson: Here is a page produced from observations we chose, so every number can be checked by hand. Read the page from the top. For each metric there is a help line, then a type line, then the samples. The counter has two lines because it has two label combinations, one per status code. The histogram expands into a line per boundary, each carrying the label l e, then the plus infinity line, then the sum and the count. Notice that the sum and the count use the metric name with a suffix rather than a label. Those suffixes are part of the convention that makes a histogram a histogram rather than a pile of counters.

## Files

- [`starter/exposition.py`](starter/exposition.py): the listing from the lesson
- [`starter/metrics.py`](starter/metrics.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l06/m02l06-02/starter`
2. Read `exposition.py`.
3. Run it: `python3 exposition.py`.
4. Check it from the repository root: `./check m02l06-02`.

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

`./check m02l06-02` copies `starter/` into a scratch directory and runs `python3 exposition.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m02l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
