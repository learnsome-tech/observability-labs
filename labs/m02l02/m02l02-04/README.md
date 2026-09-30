# m02l02-04 · Why a summary cannot be added up

**Lesson:** [Metric Types: Summaries And Histograms](https://learnsome.tech/learn/observability-course/m02l02) (lesson 2.2, module 2: Metrics And Prometheus) · Pro  
**Check:** Graded

## Goal

You can explain how a histogram stores a distribution in counters, why a summary cannot be aggregated across instances, and how to choose bucket boundaries.

In the lesson: This is the argument that settles the choice. Two instances of the same service, each with its own latency distribution, one taking percentiles directly and one counting into buckets. Look at the two answers. Averaging the two ninety ninth percentiles gives six hundred milliseconds, and the true ninety ninth percentile across both instances is nine hundred. The average of percentiles is not a percentile of anything: it is a number with no meaning that happens to look plausible on a dashboard. Now look at the buckets. You can add them position by position, because each one is a count, and the sum is a real histogram of both instances that you can take any percentile of.

## Files

- [`starter/summary_vs_histogram.py`](starter/summary_vs_histogram.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-04/starter`
2. Read `summary_vs_histogram.py`.
3. Run it: `python3 summary_vs_histogram.py`.
4. Check it from the repository root: `./check m02l02-04`.

## Expected output

```text
instance a, ninety ninth: 0.3
instance b, ninety ninth: 0.9
mean of those two: 0.6
true ninety ninth of both: 0.9
buckets a: [90, 99, 99, 100, 100]
buckets b: [50, 50, 99, 99, 100]
```

## How to check

`./check m02l02-04` copies `starter/` into a scratch directory and runs `python3 summary_vs_histogram.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
