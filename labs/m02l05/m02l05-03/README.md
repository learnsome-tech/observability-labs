# m02l05-03 · Looking at the scrape from both ends

**Lesson:** [Prometheus Scraping And The Pull Model](https://learnsome.tech/learn/observability-course/m02l05) (lesson 2.5, module 2: Metrics And Prometheus) · Pro  
**Check:** Read along

## Goal

You can describe what a scrape is, configure a target, read the health of every target, and explain what the pull model gives you that pushing does not.

In the lesson: Let us look at a real one, from both ends. In the stack directory there are five containers running. Ask Prometheus which pages it is fetching and you get three addresses: itself, the sample service, and the collector. Ask it whether each one worked and you get the up metric, one for each job, with the value one meaning the last fetch succeeded. Then check that the page itself is ordinary: fetching it by hand returns two hundred, the same as it does for Prometheus. There is no agent, no protocol and no credential in that path. It is a web page full of numbers.

## Files

- [`starter/session-looking-at-the-scrape-from-both-ends.sh`](starter/session-looking-at-the-scrape-from-both-ends.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/session-looking-at-the-scrape-from-both-ends.sh` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
