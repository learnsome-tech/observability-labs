# m03l03-04 · The quantile estimate comes from buckets

**Lesson:** [Calculating Percentiles With histogram_quantile](https://learnsome.tech/learn/observability-course/m03l03) (lesson 3.3, module 3: PromQL And Dashboards) · Pro  
**Check:** Graded

## Goal

You can read cumulative histogram buckets and use histogram quantile to estimate a percentile without pretending that an average describes the tail.

In the lesson: This is the same search in executable form. The target rank is the requested fraction of the total count. The loop finds the first cumulative bucket that reaches that rank, then interpolates between the previous boundary and the current one. The estimates are printed for the median, the ninetieth, the ninety fifth, and the ninety ninth percentile. A histogram gives Prometheus enough shape to estimate a tail, while the raw average never contained that shape in the first place.

## Files

- [`starter/histogram_quantile.py`](starter/histogram_quantile.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-04/starter`
2. Read `histogram_quantile.py`.
3. Run it: `python3 histogram_quantile.py`.
4. Check it from the repository root: `./check m03l03-04`.

## Expected output

```text
p50 0.0278
p90 0.05
p95 0.0917
p99 2.0
```

## How to check

`./check m03l03-04` copies `starter/` into a scratch directory and runs `python3 histogram_quantile.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
