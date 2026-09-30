# m02l02-02 · A histogram is just counters underneath

**Lesson:** [Metric Types: Summaries And Histograms](https://learnsome.tech/learn/observability-course/m02l02) (lesson 2.2, module 2: Metrics And Prometheus) · Pro  
**Check:** Read along

## Goal

You can explain how a histogram stores a distribution in counters, why a summary cannot be aggregated across instances, and how to choose bucket boundaries.

In the lesson: Here is the whole of observing a value. Take the number, and for every bucket whose boundary it fits under, add one. That is why buckets are called cumulative: a request of thirty milliseconds is counted in the fifty millisecond bucket and in every larger one as well. Then keep a running sum and a running count, which give you the average for free and, more usefully, let the server work out rates of both. What leaves the process is nothing but integers going up, which is why everything you learned about counters applies unchanged.

## Files

- [`starter/metrics.py`](starter/metrics.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/metrics.py` alongside the lesson.
2. Notes from the lesson:
   - Line 1: one observation, and every bucket it fits in goes up
   - Line 7: the sum and the count come along, for the average

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
