# m04l01-04 · Attributes keep values typed

**Lesson:** [OpenTelemetry: The Vendor Neutral Path](https://learnsome.tech/learn/observability-course/m04l01) (lesson 4.1, module 4: OpenTelemetry And Distributed Tracing) · Pro  
**Check:** Read along

## Goal

You can explain why OpenTelemetry separates instrumentation from storage vendors and identify the common language shared by traces, metrics, and logs.

In the lesson: This fragment from the course exporter shows the rule in code. A boolean stays a boolean, an integer stays an integer, and a floating point value stays numeric. Everything else becomes a string. Typed attributes let a backend filter and aggregate reliably, while an accidental string representation can turn a useful value into decoration. The exporter also treats a missing endpoint as a safe no operation, so telemetry trouble cannot break the request being observed.

## Files

- [`starter/otlp.py`](starter/otlp.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/otlp.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
