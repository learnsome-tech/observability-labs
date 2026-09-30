# m04l02-03 · The trace tree and header are visible

**Lesson:** [Traces, Spans And Context Propagation](https://learnsome.tech/learn/observability-course/m04l02) (lesson 4.2, module 4: OpenTelemetry And Distributed Tracing) · Pro  
**Check:** Runs, not graded

## Goal

You can read a trace tree, distinguish a parent span from a child span, and explain how trace context crosses a service boundary.

In the lesson: This executable example creates one checkout span and two child spans. The database and payment work share the trace identifier and point back to the checkout span as their parent. The final lines format a traceparent header from the payment span, parse it as a downstream service would, and confirm that the trace identifier is unchanged. The header carries enough identity to continue the tree; the receiving service does not need to know anything about the caller's implementation.

## Files

- [`starter/otlp.py`](starter/otlp.py)
- [`starter/trace_demo.py`](starter/trace_demo.py): the listing from the lesson
- [`starter/tracing.py`](starter/tracing.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-03/starter`
2. Read `trace_demo.py`.
3. Run it: `python3 trace_demo.py`.
4. Check it from the repository root: `./check m04l02-03`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
GET /checkout    span=043bae1603803a93 parent=none
SELECT basket    span=dcf4bb99f4bea973 parent=043bae1603803a93
POST payments    span=1e7c6e9fdc32a8a9 parent=043bae1603803a93
traceparent: 00-216363698b529b4a97b750923ceb3ffd-1e7c6e9fdc32a8a9-01
downstream reads: 216363698b529b4a97b750923ceb3ffd
same trace: True
```

## How to check

`./check m04l02-03` copies `starter/` into a scratch directory and runs `python3 trace_demo.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
