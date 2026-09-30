# m02l02 · Metric Types: Summaries And Histograms

Module 2: Metrics And Prometheus · lesson 2.2 · Pro · [Open the lesson](https://learnsome.tech/learn/observability-course/m02l02)

**Goal:** You can explain how a histogram stores a distribution in counters, why a summary cannot be aggregated across instances, and how to choose bucket boundaries.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l02-02](m02l02-02/) | A histogram is just counters underneath | Read along |
| [m02l02-03](m02l02-03/) | What a histogram looks like on the wire | Graded |
| [m02l02-04](m02l02-04/) | Why a summary cannot be added up | Graded |

## Check yourself

- What does the bucket labelled plus infinity always equal, and why?
- Why can two instances' histograms be added but their summaries cannot?
- What is wrong with the average of two ninety ninth percentiles?
- Where should one of your bucket boundaries always be, and what does that buy?
- What does a histogram cost that a summary does not?

---

[Course README](../../README.md) · [Full-Stack Observability: Metrics, Tracing & Logging on LearnSome.tech](https://learnsome.tech/courses/observability-course)
