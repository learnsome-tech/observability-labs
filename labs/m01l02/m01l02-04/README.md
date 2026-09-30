# m01l02-04 · A trace: one request, across everything it touched

**Lesson:** [The Three Signals: Logs, Metrics And Traces](https://learnsome.tech/learn/observability-course/m01l02) (lesson 1.2, module 1: The Foundations Of Observability) · Free  
**Check:** Graded

## Goal

You can say what a log, a metric and a trace each answer well, what each costs, and which one to reach for when something is wrong.

In the lesson: And a trace. This builds a root span for a checkout, then two children: one for the database query, one for the call to payments, which fails. Print the tree and you can read the structure straight off. Every span carries the same trace ID, so they belong to the same request, and each child carries the span ID of its parent, so the shape of the work is recoverable. The last lines show the header that carries the trace across a network boundary, and the next service parsing it back out. That is the whole trick of distributed tracing: an identifier that travels with the request, so work happening in five processes can be reassembled into one story.

## Files

- [`starter/otlp.py`](starter/otlp.py)
- [`starter/trace_demo.py`](starter/trace_demo.py): the listing from the lesson
- [`starter/tracing.py`](starter/tracing.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-04/starter`
2. Read `trace_demo.py` the way the lesson builds it:
   - Lines 1–8: a root span
   - Lines 9–14: two children
   - Lines 15–21: print the tree
3. Run it: `python3 trace_demo.py`.
4. Check it from the repository root: `./check m01l02-04`.

## Expected output

```text
GET /checkout    span=ea7b5bf55eb561a4 parent=none
SELECT basket    span=795b929e9a9a80fd parent=ea7b5bf55eb561a4
POST payments    span=94b2b8fda02f34a6 parent=ea7b5bf55eb561a4
traceparent: 00-216363698b529b4a97b750923ceb3ffd-94b2b8fda02f34a6-01
downstream reads: 216363698b529b4a97b750923ceb3ffd
same trace: True
```

## How to check

`./check m01l02-04` copies `starter/` into a scratch directory and runs `python3 trace_demo.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
