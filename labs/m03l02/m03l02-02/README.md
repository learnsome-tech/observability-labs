# m03l02-02 · A reset must not become negative work

**Lesson:** [Rates And Increases Over Time](https://learnsome.tech/learn/observability-course/m03l02) (lesson 3.2, module 3: PromQL And Dashboards) · Pro  
**Check:** Read along

## Goal

You can turn a monotonically increasing counter into a request rate, account for resets, and choose between rate and increase for a real question.

In the lesson: The counter in this example rises, restarts, and rises again. A raw subtraction sees the restart and reports negative sixty five, which would describe the world as if work had been taken away. The increase function treats a fall as a reset and adds the work after the restart. Across one minute it finds one hundred and ninety five events, or three point two five events each second. Prometheus rate and increase apply the same idea to real scraped samples.

## Files

- [`starter/counters.py`](starter/counters.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/counters.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
