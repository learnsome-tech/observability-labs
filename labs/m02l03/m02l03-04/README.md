# m02l03-04 · Where the percentile comes from, exactly

**Lesson:** [Why A Histogram Beats An Average](https://learnsome.tech/learn/observability-course/m02l03) (lesson 2.3, module 2: Metrics And Prometheus) · Pro  
**Check:** Graded

## Goal

You can show why an average hides the experience of your slowest users, read a percentile correctly, and know what a percentile drawn from buckets can and cannot tell you.

In the lesson: Prometheus never sees your individual latencies, only counted buckets, so it has to reconstruct percentiles from them. Here is exactly what it does: find the bucket that holds the rank you asked for, then assume the observations inside that bucket are spread evenly and interpolate inside it. Run the four percentiles and read the last one carefully. The ninety ninth comes back as two seconds, which is suspiciously round, and it is round because it is an artefact: the rank falls in the bucket between one and two and a half seconds, and there is nothing in there to be more precise with. That is the honest limit of the method.

## Files

- [`starter/histogram_quantile.py`](starter/histogram_quantile.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-04/starter`
2. Read `histogram_quantile.py` the way the lesson builds it:
   - Lines 1–4: counted buckets
   - Lines 5–19: Prometheus never sees your individual latencies
   - Lines 20–22: run the four percentiles
3. Run it: `python3 histogram_quantile.py`.
4. Check it from the repository root: `./check m02l03-04`.

## Expected output

```text
p50 0.0278
p90 0.05
p95 0.0917
p99 2.0
```

## How to check

`./check m02l03-04` copies `starter/` into a scratch directory and runs `python3 histogram_quantile.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
