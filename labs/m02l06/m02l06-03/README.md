# m02l06-03 · The same thing, fetched over the network

**Lesson:** [The Prometheus Exposition Format](https://learnsome.tech/learn/observability-course/m02l06) (lesson 2.6, module 2: Metrics And Prometheus) · Pro  
**Check:** Read along

## Goal

You can read and write the text format a scrape returns, including help and type lines, label syntax, histogram buckets, and the rules that make a page valid.

In the lesson: Now the same format, over the network, from the service this course ships. Start the service on a spare port, send three requests to a route that does nothing measurable, then fetch the page. The histogram lines are filtered out here so the numbers stay identical every run. What is left shows the three shapes side by side: a counter with three labels, a gauge with none, and a second gauge carrying a version string as a label with a constant value of one. That last pattern is called an info metric, and it is how you attach build information to a service without inventing a new kind of metric.

## Files

- [`starter/exposition_demo.sh`](starter/exposition_demo.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/exposition_demo.sh` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–7: start the service
   - Lines 8–11: three requests to a route that does nothing
   - Lines 12–13: fetch the page

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l06-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m02l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
