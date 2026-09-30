# m04l04-03 · The service emits all three signals

**Lesson:** [Instrumenting A Service With Client Libraries](https://learnsome.tech/learn/observability-course/m04l04) (lesson 4.4, module 4: OpenTelemetry And Distributed Tracing) · Pro  
**Check:** Read along

## Goal

You can identify the instrumentation points in a real service and explain what a client library should record automatically versus what your code must name explicitly.

In the lesson: The sample service ties the ideas together in its request handler. It reads incoming context, creates a span, performs the work, records a counter and a histogram, writes a structured log with the trace identifier, and exports the finished span. The full service is longer than one editor pane, so this lesson marks the listing as a fragment. The important ordering is visible in the source: context first, work second, signals around the work, and response last.

## Files

- [`starter/app.py`](starter/app.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/app.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
