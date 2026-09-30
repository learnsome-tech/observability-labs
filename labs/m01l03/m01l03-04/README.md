# m01l03-04 · Now a question is a query, not a regular expression

**Lesson:** [Structured Logging And Why Text Fails](https://learnsome.tech/learn/observability-course/m01l03) (lesson 1.3, module 1: The Foundations Of Observability) · Free  
**Check:** Graded

## Goal

You can write log events as records with stable field names, explain why a sentence is not a log, and query your own logs without a regular expression.

In the lesson: With records, asking is cheap. Load the records, one per line. Ask how many were large by comparing a number with a number, ask what the total came to by adding a field up, ask which users appear by collecting a field. Run it and the answers come out. In production you would type this into a log system rather than write it in a file, but the shape is identical, and so is the important property: these questions were not designed in. Nobody added a counter for orders over fifty pounds. The fields were kept honestly, and that was enough to answer a question invented afterwards.

## Files

- [`starter/orders.jsonl`](starter/orders.jsonl)
- [`starter/query_logs.py`](starter/query_logs.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-04/starter`
2. Read `query_logs.py` the way the lesson builds it:
   - Lines 1–9: load the records
   - Lines 10–11: how many were large
   - Lines 12–14: and the answers come out
3. Run it: `python3 query_logs.py`.
4. Check it from the repository root: `./check m01l03-04`.

## Expected output

```text
events: 3
over fifty pounds: 1
total: 114.99
by user: ['u1', 'u4']
```

## How to check

`./check m01l03-04` copies `starter/` into a scratch directory and runs `python3 query_logs.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
