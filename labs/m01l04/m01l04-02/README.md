# m01l04-02 · Levels as numbers, and one threshold

**Lesson:** [Log Levels Done Properly](https://learnsome.tech/learn/observability-course/m01l04) (lesson 1.4, module 1: The Foundations Of Observability) · Free  
**Check:** Read along

## Goal

You can choose the right level for an event, set a threshold at run time rather than at build time, and stop using error for things that are not errors.

In the lesson: Mechanically, a level system is trivial. A number for each level, so they can be compared. A threshold, read from the environment when the process starts, so the running service can be made noisier without a rebuild and without a code review. Then one comparison at the top of the log function, and quieter records cost almost nothing. Two details matter here. The threshold is configuration, not a constant, because the moment you need debug output is the moment you cannot wait for a deploy. And the comparison happens before the record is built, so a debug line in a hot path does not pay for formatting that nobody will read.

## Files

- [`starter/logs.py`](starter/logs.py): the listing from the lesson
- [`starter/otlp.py`](starter/otlp.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/logs.py` alongside the lesson.
2. Notes from the lesson:
   - Line 1: a number per level, so comparing them is possible
   - Line 3: the threshold comes from the environment at start up

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
