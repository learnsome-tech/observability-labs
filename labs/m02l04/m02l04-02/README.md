# m02l04-02 · Do the multiplication before you ship

**Lesson:** [Cardinality And How It Bankrupts You](https://learnsome.tech/learn/observability-course/m02l04) (lesson 2.4, module 2: Metrics And Prometheus) · Pro  
**Check:** Graded

## Goal

You can count the series a metric will create before you ship it, recognise the labels that must never exist, and say where high cardinality data belongs instead.

In the lesson: Here is the calculation nobody does before shipping. Four sensible labels: a handful of methods, twenty routes, a few status codes, a dozen instances. Multiply them together and you get under six thousand series and about eighteen megabytes, which is nothing. Now add one apparently innocent label, a user identifier, with fifty thousand distinct values. The series count becomes two hundred and eighty eight million and the memory estimate is nine hundred gigabytes. Nobody typed nine hundred gigabytes. Somebody typed one extra label in one line of code, in a pull request that looked helpful, and the reviewer thought it seemed useful to have.

## Files

- [`starter/cardinality.py`](starter/cardinality.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-02/starter`
2. Read `cardinality.py` the way the lesson builds it:
   - Lines 1–4: four sensible labels
   - Lines 5–16: multiply them together
   - Lines 17–19: add one apparently innocent label
3. Run it: `python3 cardinality.py`.
4. Check it from the repository root: `./check m02l04-02`.

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

`./check m02l04-02` copies `starter/` into a scratch directory and runs `python3 cardinality.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
