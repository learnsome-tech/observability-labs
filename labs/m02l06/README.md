# m02l06 · The Prometheus Exposition Format

Module 2: Metrics And Prometheus · lesson 2.6 · Pro · [Open the lesson](https://learnsome.tech/learn/observability-course/m02l06)

**Goal:** You can read and write the text format a scrape returns, including help and type lines, label syntax, histogram buckets, and the rules that make a page valid.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l06-02](m02l06-02/) | A page, rendered from known observations | Graded |
| [m02l06-03](m02l06-03/) | The same thing, fetched over the network | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn

1. Write a page by hand with one counter and one gauge, with help and type
2. Serve it with any web server and add it to the scrape configuration
3. Break it on purpose: repeat a series, and see what the target health says

> **Hint:** A static file served over the network is a perfectly legal target.

## Check yourself

- What are the three parts of a sample line?
- What do the two hash comment lines above a metric declare?
- How does a histogram appear in the text format, and which label carries the boundary?
- What is an info metric and why is its value always one?
- What does an exemplar add, and why is that useful during an incident?

---

[Course README](../../README.md) · [Full-Stack Observability: Metrics, Tracing & Logging on LearnSome.tech](https://learnsome.tech/courses/observability-course)
