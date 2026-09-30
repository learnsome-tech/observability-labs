# m03l04-03 · The helper uses the Prometheus query endpoint

**Lesson:** [Grafana: Connecting The Data Source](https://learnsome.tech/learn/observability-course/m03l04) (lesson 3.4, module 3: PromQL And Dashboards) · Pro  
**Check:** Read along

## Goal

You can connect Grafana to Prometheus, run a query in Explore, and distinguish a data source problem from a query problem.

In the lesson: This helper makes the connection visible without a browser. It sends a PromQL expression to the Prometheus query endpoint, chooses a fixed recorded time by default, and prints the labelled results. In Grafana, Explore performs the same exchange for you. The helper is a transcript here when the local stack is unavailable, but the file is still checked against the shipped artifact. That distinction matters: the query is concrete, while the screen claim is marked honestly when its server cannot run.

## Files

- [`starter/query.sh`](starter/query.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/query.sh` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
