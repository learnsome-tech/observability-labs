# m02l05-02 · The configuration that defines a target

**Lesson:** [Prometheus Scraping And The Pull Model](https://learnsome.tech/learn/observability-course/m02l05) (lesson 2.5, module 2: Metrics And Prometheus) · Pro  
**Check:** Checker

## Goal

You can describe what a scrape is, configure a target, read the health of every target, and explain what the pull model gives you that pushing does not.

In the lesson: Here is the whole configuration for the stack this course runs. There is a global section saying how often to fetch and how often to evaluate rules. There is a list of rule files, which we come back to in the alerting module. And there is a list of scrape jobs. A job is a group of targets doing the same work, and every series that comes from it is labelled with the job name automatically, along with the instance it came from. In a real cluster the list of targets comes from service discovery rather than being written out, but the shape is identical: a job, and some addresses.

## Files

- [`starter/prometheus.yml`](starter/prometheus.yml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-02/starter`
2. Read `prometheus.yml`.
3. Notes from the lesson:
   - Line 3: how often every target is fetched, unless overridden
   - Line 16: a job is a set of targets doing the same work
4. Edit `prometheus.yml` and check it: `yamllint prometheus.yml`.
5. Check it from the repository root: `./check m02l05-02`.
6. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m02l05-02 --command=<id>`:
   - `lint` (Lint): `yamllint -d relaxed prometheus.yml`
   - `strict` (Lint strictly): `yamllint prometheus.yml`

## How to check

`./check m02l05-02` copies `starter/` into a scratch directory and runs `yamllint prometheus.yml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
