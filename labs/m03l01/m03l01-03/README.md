# m03l01-03 · Selectors return labelled series

**Lesson:** [PromQL Basics And Selectors](https://learnsome.tech/learn/observability-course/m03l01) (lesson 3.1, module 3: PromQL And Dashboards) · Pro  
**Check:** Graded

## Goal

You can select a Prometheus series with labels, read an instant vector, and explain why a query result is a set of time series rather than a single number.

In the lesson: This small program is not PromQL, but it shows what a selector is choosing from. Four dimensions multiply into five thousand seven hundred and sixty possible series. Add a user identifier and the family becomes two hundred and eighty eight million. A selector can only be as healthy as the labels behind it. Query language makes the combinations easy to read, while the storage cost remains very real. The first PromQL habit is therefore to inspect the labels before you aggregate them.

## Files

- [`starter/cardinality.py`](starter/cardinality.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-03/starter`
2. Read `cardinality.py`.
3. Run it: `python3 cardinality.py`.
4. Check it from the repository root: `./check m03l01-03`.

## Expected output

```text
labels: ['method', 'route', 'status', 'instance']
series: 5760
memory mb: 18.4
---
labels: ['method', 'route', 'status', 'instance', 'user_id']
series: 288000000
memory mb: 921600.0
```

## How to check

`./check m03l01-03` copies `starter/` into a scratch directory and runs `python3 cardinality.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
