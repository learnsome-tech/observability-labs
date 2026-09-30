# m01l02-02 · A metric: cheap, aggregated, no identity at all

**Lesson:** [The Three Signals: Logs, Metrics And Traces](https://learnsome.tech/learn/observability-course/m01l02) (lesson 1.2, module 1: The Foundations Of Observability) · Free  
**Check:** Read along

## Goal

You can say what a log, a metric and a trace each answer well, what each costs, and which one to reach for when something is wrong.

In the lesson: Start with a metric. Here is a script that starts the service this course ships, on a spare port, then sends it exactly twenty requests, then scrapes it once and prints the counters. Look at what comes back. Three lines of numbers cover twenty requests, grouped by route and by status code. That is the bargain a metric makes: it throws away everything about the individual request and keeps a count, so the cost hardly grows as traffic grows. Twenty requests, twenty million requests, still three lines. And notice what you cannot ask it. Which customer got the not found? You have no idea, and this metric will never tell you.

## Files

- [`starter/scrape_demo.sh`](starter/scrape_demo.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/scrape_demo.sh` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: a script that starts the service
   - Lines 8–11: sends it exactly twenty requests
   - Lines 12–13: scrapes it once

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
