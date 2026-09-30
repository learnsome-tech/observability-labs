# m03l01 · PromQL Basics And Selectors

Module 3: PromQL And Dashboards · lesson 3.1 · Pro · [Open the lesson](https://learnsome.tech/learn/observability-course/m03l01)

**Goal:** You can select a Prometheus series with labels, read an instant vector, and explain why a query result is a set of time series rather than a single number.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l01-03](m03l01-03/) | Selectors return labelled series | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Ask three precise questions

1. Select one route from the demo request metric
2. Select only server errors with a status matcher
3. Aggregate by route and explain which labels disappear

> **Hint:** Say the question in words before writing its selector.

## Check yourself

- What does a metric name select?
- How do exact and regular expression matchers differ?
- What information stays attached to an instant vector?
- Why can count be useful before an aggregation?
- What should you say before writing a selector?

---

[Course README](../../README.md) · [Full-Stack Observability: Metrics, Tracing & Logging on LearnSome.tech](https://learnsome.tech/courses/observability-course)
