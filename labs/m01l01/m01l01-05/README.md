# m01l01-05 · A new question, answered from data you already have

**Lesson:** [Observability Versus Monitoring](https://learnsome.tech/learn/observability-course/m01l01) (lesson 1.1, module 1: The Foundations Of Observability) · Free  
**Check:** Graded

## Goal

You can say what monitoring is good at, what observability adds, and why a green health check is not evidence that a service is working.

In the lesson: This is the other half of the idea, in fourteen lines. Nobody built a dashboard called orders over fifty pounds. Nobody needed to, because the events were recorded as data rather than as sentences, so a new question is a few lines of code against evidence that already exists. The records are loaded, then we ask how many were large, then what the total came to, and who was involved. Run the questions and you get answers to things nobody planned for. Hold on to that feeling, because it is the whole course: emit evidence with enough structure and enough detail that tomorrow's question, which you cannot guess today, is a query rather than a release.

## Files

- [`starter/orders.jsonl`](starter/orders.jsonl)
- [`starter/query_logs.py`](starter/query_logs.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-05/starter`
2. Read `query_logs.py` the way the lesson builds it:
   - Lines 1–8: the records are loaded
   - Lines 9–11: how many were large
   - Lines 12–14: and who was involved
3. Run it: `python3 query_logs.py`.
4. Check it from the repository root: `./check m01l01-05`.

## Expected output

```text
events: 3
over fifty pounds: 1
total: 114.99
by user: ['u1', 'u4']
```

## How to check

`./check m01l01-05` copies `starter/` into a scratch directory and runs `python3 query_logs.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
