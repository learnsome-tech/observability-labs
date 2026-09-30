# m03l02 · Rates And Increases Over Time

Module 3: PromQL And Dashboards · lesson 3.2 · Pro · [Open the lesson](https://learnsome.tech/learn/observability-course/m03l02)

**Goal:** You can turn a monotonically increasing counter into a request rate, account for resets, and choose between rate and increase for a real question.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l02-02](m03l02-02/) | A reset must not become negative work | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Choose a window and defend it

1. Write a rate for total requests over a short window
2. Write an increase for a daily request count
3. Explain what a restart should look like in both results

> **Hint:** Name the window and the unit in your explanation.

## Check yourself

- Why is a counter value alone a poor traffic measure?
- How should a reset affect an increase?
- When would increase be clearer than rate?
- Why calculate rates before aggregating instances?
- What tradeoff does a short window create?

---

[Course README](../../README.md) · [Full-Stack Observability: Metrics, Tracing & Logging on LearnSome.tech](https://learnsome.tech/courses/observability-course)
