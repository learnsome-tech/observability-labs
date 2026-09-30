# m01l03-05 · The logger the service in this course uses

**Lesson:** [Structured Logging And Why Text Fails](https://learnsome.tech/learn/observability-course/m01l03) (lesson 1.3, module 1: The Foundations Of Observability) · Free  
**Check:** Read along

## Goal

You can write log events as records with stable field names, explain why a sentence is not a log, and query your own logs without a regular expression.

In the lesson: This is the logger the sample service uses, and it is deliberately tiny. There is a level threshold read from the environment, so the running service can be made noisier without a code change. There is one function. It builds a dictionary with four fields on every single record: when, how serious, which service, and what happened. Then it merges in whatever the caller passed, writes one line of data, and flushes. That is the entire thing. Everything else in this lesson is a convention rather than a library: stable names, a constant event, values that are values rather than sentences.

## Files

- [`starter/logs.py`](starter/logs.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/logs.py` alongside the lesson.
2. Notes from the lesson:
   - Line 6: one threshold, read once, from the environment
   - Line 13: four fields on every record, then whatever the caller adds

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
