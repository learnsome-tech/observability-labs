# m02l01 · Metric Types: Counters And Gauges

Module 2: Metrics And Prometheus · lesson 2.1 · Pro · [Open the lesson](https://learnsome.tech/learn/observability-course/m02l01)

**Goal:** You can choose between a counter and a gauge for any measurement, name them the way Prometheus expects, and explain why a counter is only useful once you take its rate.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l01-02](m02l01-02/) | The same events, counted two ways | Graded |
| [m02l01-03](m02l01-03/) | A counter, in full | Read along |
| [m02l01-04](m02l01-04/) | Why a counter is useless until you ask about time | Graded |

## Check yourself

- Which type would you use for jobs currently waiting, and which for jobs ever enqueued?
- What does a counter do at a process restart, and how does a rate survive it?
- Why should a duration metric be measured in seconds rather than milliseconds?
- Why is a separate metric name per status worse than one metric with a status label?
- What kind of event can a gauge miss completely, and why?

---

[Course README](../../README.md) · [Full-Stack Observability: Metrics, Tracing & Logging on LearnSome.tech](https://learnsome.tech/courses/observability-course)
