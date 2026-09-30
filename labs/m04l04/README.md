# m04l04 · Instrumenting A Service With Client Libraries

Module 4: OpenTelemetry And Distributed Tracing · lesson 4.4 · Pro · [Open the lesson](https://learnsome.tech/learn/observability-course/m04l04)

**Goal:** You can identify the instrumentation points in a real service and explain what a client library should record automatically versus what your code must name explicitly.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l04-03](m04l04-03/) | The service emits all three signals | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Mark the instrumentation points

1. Circle where a request span begins and ends
2. Name one safe business attribute
3. Name one label that would create bad cardinality

> **Hint:** Follow one request through the handler before choosing fields.

## Check yourself

- What can a client library automate?
- Which details must application code name?
- Why should secrets stay out of attributes?
- How can trace volume be controlled?
- What makes a label unsafe?

---

[Course README](../../README.md) · [Full-Stack Observability: Metrics, Tracing & Logging on LearnSome.tech](https://learnsome.tech/courses/observability-course)
