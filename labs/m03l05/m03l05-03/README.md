# m03l05-03 · The data tells a different story by percentile

**Lesson:** [Dashboards That Answer Questions](https://learnsome.tech/learn/observability-course/m03l05) (lesson 3.5, module 3: PromQL And Dashboards) · Pro  
**Check:** Graded

## Goal

You can design a focused dashboard around a user facing question, choose panels that support it, and remove decoration that cannot guide a decision.

In the lesson: Suppose the question is whether customers are waiting too long. A panel showing only the mean would report about ninety six milliseconds and invite a reassuring green colour. The percentile view says the median and ninetieth percentile are forty, while the ninety ninth is one thousand five hundred. That changes the decision: investigate the tail, do not celebrate the average. The same data becomes useful when the panel title names the customer question instead of naming the implementation detail.

## Files

- [`starter/average_lies.py`](starter/average_lies.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-03/starter`
2. Read `average_lies.py`.
3. Run it: `python3 average_lies.py`.
4. Check it from the repository root: `./check m03l05-03`.

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

`./check m03l05-03` copies `starter/` into a scratch directory and runs `python3 average_lies.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
