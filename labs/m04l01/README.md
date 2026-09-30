# m04l01 · OpenTelemetry: The Vendor Neutral Path

Module 4: OpenTelemetry And Distributed Tracing · lesson 4.1 · Pro · [Open the lesson](https://learnsome.tech/learn/observability-course/m04l01)

**Goal:** You can explain why OpenTelemetry separates instrumentation from storage vendors and identify the common language shared by traces, metrics, and logs.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l01-04](m04l01-04/) | Attributes keep values typed | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Choose the boundary for your service

1. List the signals your service emits
2. Name the collector receiver that accepts them
3. Name the backend that should remain replaceable

> **Hint:** Keep the service code about meaning and the platform code about routing.

## Check yourself

- Why should instrumentation outlive a vendor?
- What do resource attributes identify?
- What work belongs in a collector?
- Why do typed attributes matter?
- Where should routing decisions live?

---

[Course README](../../README.md) · [Full-Stack Observability: Metrics, Tracing & Logging on LearnSome.tech](https://learnsome.tech/courses/observability-course)
