# m04l03-02 · The shipped collector routes traces and logs

**Lesson:** [The OpenTelemetry Collector](https://learnsome.tech/learn/observability-course/m04l03) (lesson 4.3, module 4: OpenTelemetry And Distributed Tracing) · Pro  
**Check:** Checker

## Goal

You can read a collector pipeline, explain receivers processors and exporters, and describe why batching and memory limits belong at the boundary.

In the lesson: This is the collector configuration shipped with the course. It receives traces over both common OpenTelemetry transports, batches them, protects memory, and exports traces for inspection. Its log pipeline sends records onward to Loki. The configuration is shown as a transcript here because the collector cannot run on this machine without Docker, but it is the exact file the stack consumes. The important reading order is receiver, processor, exporter, then pipeline.

## Files

- [`starter/collector.yaml`](starter/collector.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-02/starter`
2. Read `collector.yaml`.
3. Edit `collector.yaml` and check it: `yamllint collector.yaml`.
4. Check it from the repository root: `./check m04l03-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m04l03-02 --command=<id>`:
   - `lint` (Lint): `yamllint -d relaxed collector.yaml`
   - `strict` (Lint strictly): `yamllint collector.yaml`

## How to check

`./check m04l03-02` copies `starter/` into a scratch directory and runs `yamllint collector.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
