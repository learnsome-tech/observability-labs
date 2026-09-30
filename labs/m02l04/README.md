# m02l04 · Cardinality And How It Bankrupts You

Module 2: Metrics And Prometheus · lesson 2.4 · Pro · [Open the lesson](https://learnsome.tech/learn/observability-course/m02l04)

**Goal:** You can count the series a metric will create before you ship it, recognise the labels that must never exist, and say where high cardinality data belongs instead.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l04-02](m02l04-02/) | Do the multiplication before you ship | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn

1. List the labels on the busiest metric in your own service
2. Write down the realistic number of distinct values for each
3. Multiply them, and then add an instance count and a bucket count

> **Hint:** Histogram buckets multiply everything: ten boundaries is ten times.

## Check yourself

- Why is the series count a product rather than a sum?
- Name four label values that must never appear on a metric.
- Why is the raw request path dangerous, and what do you use instead?
- Where should per request detail live, and what joins it back to your metrics?
- Why do incidents make a cardinality problem worse at the worst moment?

---

[Course README](../../README.md) · [Full-Stack Observability: Metrics, Tracing & Logging on LearnSome.tech](https://learnsome.tech/courses/observability-course)
