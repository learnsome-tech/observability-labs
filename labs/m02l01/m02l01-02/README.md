# m02l01-02 · The same events, counted two ways

**Lesson:** [Metric Types: Counters And Gauges](https://learnsome.tech/learn/observability-course/m02l01) (lesson 2.1, module 2: Metrics And Prometheus) · Pro  
**Check:** Graded

## Goal

You can choose between a counter and a gauge for any measurement, name them the way Prometheus expects, and explain why a counter is only useful once you take its rate.

In the lesson: Here is a queue over five rounds, with arrivals and departures in each round, measured by one counter and one gauge. The counter records everything that ever arrived. The gauge records how many are waiting at the end of each round. Run the five rounds and watch the columns. The left column never falls, even in the round where more work left than arrived. The right column moves both ways, and in the third round it drops sharply. Ask yourself which column answers which question. How busy have we been since start up is the left. Are we falling behind right now is the right. They are both correct and they are not interchangeable.

## Files

- [`starter/counter_vs_gauge.py`](starter/counter_vs_gauge.py): the listing from the lesson
- [`starter/metrics.py`](starter/metrics.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-02/starter`
2. Read `counter_vs_gauge.py` the way the lesson builds it:
   - Lines 1–9: arrivals and departures
   - Lines 10–12: one counter and one gauge
   - Lines 13–19: run the five rounds
3. Run it: `python3 counter_vs_gauge.py`.
4. Check it from the repository root: `./check m02l01-02`.

## Expected output

```text
enqueued so far   3.0   waiting now   2.0
enqueued so far   8.0   waiting now   5.0
enqueued so far   8.0   waiting now   1.0
enqueued so far  12.0   waiting now   2.0
enqueued so far  14.0   waiting now   2.0
```

## How to check

`./check m02l01-02` copies `starter/` into a scratch directory and runs `python3 counter_vs_gauge.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
