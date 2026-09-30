# m02l03-02 · One hundred requests, and two honest summaries

**Lesson:** [Why A Histogram Beats An Average](https://learnsome.tech/learn/observability-course/m02l03) (lesson 2.3, module 2: Metrics And Prometheus) · Pro  
**Check:** Graded

## Goal

You can show why an average hides the experience of your slowest users, read a percentile correctly, and know what a percentile drawn from buckets can and cannot tell you.

In the lesson: Here are a hundred real shaped latencies: ninety fast requests, a few middling ones, and four that went badly wrong. The function sorts them and picks by rank, which is the simplest honest definition of a percentile. Run it and compare the lines. The mean is ninety six milliseconds, which any team would call healthy. The median is forty. But the ninety ninth percentile is one and a half seconds, and two requests in a hundred took longer than a second. Same data, three stories. The mean said healthy, the median said very healthy, and the tail said that one customer in fifty is having a bad time right now.

## Files

- [`starter/average_lies.py`](starter/average_lies.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-02/starter`
2. Read `average_lies.py` the way the lesson builds it:
   - Lines 1–3: ninety fast requests
   - Lines 4–10: Here are a hundred real shaped latencies
   - Lines 11–18: run it and compare
3. Run it: `python3 average_lies.py`.
4. Check it from the repository root: `./check m02l03-02`.

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

`./check m02l03-02` copies `starter/` into a scratch directory and runs `python3 average_lies.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
