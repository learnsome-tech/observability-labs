# m02l03 · Why A Histogram Beats An Average

Module 2: Metrics And Prometheus · lesson 2.3 · Pro · [Open the lesson](https://learnsome.tech/learn/observability-course/m02l03)

**Goal:** You can show why an average hides the experience of your slowest users, read a percentile correctly, and know what a percentile drawn from buckets can and cannot tell you.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l03-02](m02l03-02/) | One hundred requests, and two honest summaries | Graded |
| [m02l03-04](m02l03-04/) | Where the percentile comes from, exactly | Graded |

## Check yourself

- Say what the ninety ninth percentile means in one sentence, without the word worst.
- Why can the mean look healthy while one customer in fifty is suffering?
- Why did the ninety ninth percentile in the demo come back as a suspiciously round number?
- What happens to tail percentiles when your largest bucket boundary is too small?
- Rewrite average latency under two hundred milliseconds as a proper objective.

---

[Course README](../../README.md) · [Full-Stack Observability: Metrics, Tracing & Logging on LearnSome.tech](https://learnsome.tech/courses/observability-course)
