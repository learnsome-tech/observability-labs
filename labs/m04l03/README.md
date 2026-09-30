# m04l03 · The OpenTelemetry Collector

Module 4: OpenTelemetry And Distributed Tracing · lesson 4.3 · Pro · [Open the lesson](https://learnsome.tech/learn/observability-course/m04l03)

**Goal:** You can read a collector pipeline, explain receivers processors and exporters, and describe why batching and memory limits belong at the boundary.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l03-02](m04l03-02/) | The shipped collector routes traces and logs | Checker |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Trace one record through the pipeline

1. Name the receiver that accepts a trace
2. Name the processor that protects memory
3. Name the exporter that receives the processed record

> **Hint:** Read the configuration from top to bottom before looking at the pipelines.

## Check yourself

- What are the three collector stages?
- Why does batching help?
- What does a memory limiter protect?
- How should an unavailable exporter affect requests?
- How do you notice dropped telemetry?

---

[Course README](../../README.md) · [Full-Stack Observability: Metrics, Tracing & Logging on LearnSome.tech](https://learnsome.tech/courses/observability-course)
