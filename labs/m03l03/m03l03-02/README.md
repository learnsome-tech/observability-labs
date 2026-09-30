# m03l03-02 · The average hides the painful tail

**Lesson:** [Calculating Percentiles With histogram_quantile](https://learnsome.tech/learn/observability-course/m03l03) (lesson 3.3, module 3: PromQL And Dashboards) · Pro  
**Check:** Graded

## Goal

You can read cumulative histogram buckets and use histogram quantile to estimate a percentile without pretending that an average describes the tail.

In the lesson: Here are one hundred requests. The mean is about ninety six milliseconds, which sounds healthy until you look at rank. The median and the ninetieth percentile are both forty milliseconds because most requests are quick. The ninety ninth percentile is one thousand five hundred milliseconds, and two requests took more than one second. The average blended those painful requests into a number that sounds calm. Percentiles keep the customer experience at the edge of the distribution where an outage often begins.

## Files

- [`starter/average_lies.py`](starter/average_lies.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-02/starter`
2. Read `average_lies.py`.
3. Run it: `python3 average_lies.py`.
4. Check it from the repository root: `./check m03l03-02`.

## Expected output

```text
requests: 100
mean ms: 95.9
median ms: 40
p90 ms: 40
p99 ms: 1500
slower than one second: 2
```

## How to check

`./check m03l03-02` copies `starter/` into a scratch directory and runs `python3 average_lies.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
