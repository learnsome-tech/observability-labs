# m04l02 · Traces, Spans And Context Propagation

Module 4: OpenTelemetry And Distributed Tracing · lesson 4.2 · Pro · [Open the lesson](https://learnsome.tech/learn/observability-course/m04l02)

**Goal:** You can read a trace tree, distinguish a parent span from a child span, and explain how trace context crosses a service boundary.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l02-03](m04l02-03/) | The trace tree and header are visible | Runs, not graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Follow one request across two services

1. Draw the parent and child spans for a checkout request
2. Write which header carries the context
3. Mark the span where the deliberate failure occurs

> **Hint:** Keep the trace identifier constant and change the parent span identifier.

## Check yourself

- What does a trace identifier join?
- Why does each child need its own span identifier?
- What does the traceparent header carry?
- What should span attributes describe?
- How should a missing context be handled?

---

[Course README](../../README.md) · [Full-Stack Observability: Metrics, Tracing & Logging on LearnSome.tech](https://learnsome.tech/courses/observability-course)
