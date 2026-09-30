# m02l01-03 · A counter, in full

**Lesson:** [Metric Types: Counters And Gauges](https://learnsome.tech/learn/observability-course/m02l01) (lesson 2.1, module 2: Metrics And Prometheus) · Pro  
**Check:** Read along

## Goal

You can choose between a counter and a gauge for any measurement, name them the way Prometheus expects, and explain why a counter is only useful once you take its rate.

In the lesson: This is the entire implementation of a counter in the library this course ships. It declares its type, because the page a scrape fetches announces the type of every metric. It holds a dictionary keyed by the label values, so there is one stored value for each combination of labels, and the increase function adds to whichever one matches. There is no decrease function, and that absence is deliberate: a counter that can go down is a gauge wearing a disguise, and every tool downstream that assumes monotonic growth will produce nonsense from it.

## Files

- [`starter/metrics.py`](starter/metrics.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/metrics.py` alongside the lesson.
2. Notes from the lesson:
   - Line 3: the type is declared, because the scrape page announces it
   - Line 12: one stored value per combination of label values

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
