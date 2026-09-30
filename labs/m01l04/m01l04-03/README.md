# m01l04-03 · The same program, three thresholds

**Lesson:** [Log Levels Done Properly](https://learnsome.tech/learn/observability-course/m01l04) (lesson 1.4, module 1: The Foundations Of Observability) · Free  
**Check:** Read along

## Goal

You can choose the right level for an event, set a threshold at run time rather than at build time, and stop using error for things that are not errors.

In the lesson: Watch the same program at three settings. Change into the logs directory and run it as it comes: the default threshold is information, so the debug line is dropped and three records appear. Now ask for everything, and the cache lookup shows up as well, which is the line you want while reproducing a fault and never want in production. Now ask for only the losses, and a single record comes back, the one where work actually failed. Same code, same events, three different volumes, chosen at start time by an environment variable. That is the whole feature, and it is worth wiring up properly on day one.

## Files

- [`starter/session-the-same-program-three-thresholds.sh`](starter/session-the-same-program-three-thresholds.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/session-the-same-program-three-thresholds.sh` alongside the lesson.

## How to check

**Read along.** The listing does not run cleanly in the lab sandbox (it relies on something the sandbox cannot provide), so the site shows it read-only.

There is nothing to check: `./check m01l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
