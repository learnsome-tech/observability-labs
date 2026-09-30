# m01l04 · Log Levels Done Properly

Module 1: The Foundations Of Observability · lesson 1.4 · Free · [Open the lesson](https://learnsome.tech/learn/observability-course/m01l04)

**Goal:** You can choose the right level for an event, set a threshold at run time rather than at build time, and stop using error for things that are not errors.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l04-02](m01l04-02/) | Levels as numbers, and one threshold | Read along |
| [m01l04-03](m01l04-03/) | The same program, three thresholds | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn

1. Find a place in your own service that logs an error for an expected case
2. Decide whether the user got their result, and move the level accordingly
3. Then check the same failure is not logged again further up the stack

> **Hint:** The question to ask is: did somebody lose work? Not: did it look scary?

## Check yourself

- What is the honest test for whether an event deserves the error level?
- Why should the threshold come from the environment rather than from the code?
- What goes wrong when the same failure is logged at every layer?
- Which level pages somebody, and what actually does the paging?
- Name two things that belong at debug and never in production.

---

[Course README](../../README.md) · [Full-Stack Observability: Metrics, Tracing & Logging on LearnSome.tech](https://learnsome.tech/courses/observability-course)
