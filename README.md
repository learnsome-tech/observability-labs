<img src="https://learnsome.tech/logo.png" width="48" alt="LearnSome.tech">

# Full-Stack Observability: Metrics, Tracing & Logging

6 modules, 28 lessons: The Foundations Of Observability; Metrics And Prometheus; PromQL And Dashboards; OpenTelemetry And Distributed Tracing; Alerting And Reliability; Incident Response And Postmortems.

## Watch and read

- **Course page**: [https://learnsome.tech/courses/observability-course](https://learnsome.tech/courses/observability-course)
- **Video player**: [https://learnsome.tech/courses/observability-course/watch](https://learnsome.tech/courses/observability-course/watch)
- **Handbook PDF**: [https://learnsome.tech/handbooks/observability/book.pdf](https://learnsome.tech/handbooks/observability/book.pdf)
- **On-site handbook**: [https://learnsome.tech/courses/observability-course/book](https://learnsome.tech/courses/observability-course/book)

## What is in this repository

This repository contains code artifacts, exercises and reference files for the lessons in this course.
22 lessons include a `labs/<lessonId>/` folder.
Each folder is named after the lesson identifier (e.g. `labs/m01l01/`) and contains the
artifact files shown in the course video, an `EXERCISES.md` with hands-on tasks, and
sub-directories named by artifact reference (e.g. `m01l01-02/`).

## Lessons

| # | Lesson | Watch | Labs | Handbook |
|---|--------|-------|------|----------|
| | **The Foundations Of Observability** | | | |
| 1 | Observability Versus Monitoring | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m01l01) | [labs/m01l01/](labs/m01l01/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-1-1) |
| 2 | The Three Signals: Logs, Metrics And Traces | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m01l02) | [labs/m01l02/](labs/m01l02/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-1-2) |
| 3 | Structured Logging And Why Text Fails | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m01l03) | [labs/m01l03/](labs/m01l03/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-1-3) |
| 4 | Log Levels Done Properly | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m01l04) | [labs/m01l04/](labs/m01l04/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-1-4) |
| | **Metrics And Prometheus** | | | |
| 5 | Metric Types: Counters And Gauges | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m02l01) | [labs/m02l01/](labs/m02l01/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-2-1) |
| 6 | Metric Types: Summaries And Histograms | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m02l02) | [labs/m02l02/](labs/m02l02/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-2-2) |
| 7 | Why A Histogram Beats An Average | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m02l03) | [labs/m02l03/](labs/m02l03/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-2-3) |
| 8 | Cardinality And How It Bankrupts You | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m02l04) | [labs/m02l04/](labs/m02l04/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-2-4) |
| 9 | Prometheus Scraping And The Pull Model | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m02l05) | [labs/m02l05/](labs/m02l05/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-2-5) |
| 10 | The Prometheus Exposition Format | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m02l06) | [labs/m02l06/](labs/m02l06/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-2-6) |
| | **PromQL And Dashboards** | | | |
| 11 | PromQL Basics And Selectors | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m03l01) | [labs/m03l01/](labs/m03l01/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-3-1) |
| 12 | Rates And Increases Over Time | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m03l02) | [labs/m03l02/](labs/m03l02/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-3-2) |
| 13 | Calculating Percentiles With histogram_quantile | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m03l03) | [labs/m03l03/](labs/m03l03/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-3-3) |
| 14 | Grafana: Connecting The Data Source | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m03l04) | [labs/m03l04/](labs/m03l04/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-3-4) |
| 15 | Dashboards That Answer Questions | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m03l05) | [labs/m03l05/](labs/m03l05/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-3-5) |
| | **OpenTelemetry And Distributed Tracing** | | | |
| 16 | OpenTelemetry: The Vendor Neutral Path | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m04l01) | [labs/m04l01/](labs/m04l01/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-4-1) |
| 17 | Traces, Spans And Context Propagation | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m04l02) | [labs/m04l02/](labs/m04l02/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-4-2) |
| 18 | The OpenTelemetry Collector | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m04l03) | [labs/m04l03/](labs/m04l03/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-4-3) |
| 19 | Instrumenting A Service With Client Libraries | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m04l04) | [labs/m04l04/](labs/m04l04/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-4-4) |
| 20 | Bringing The Three Signals Together | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m04l05) | — | [§](https://learnsome.tech/courses/observability-course/book#lesson-4-5) |
| | **Alerting And Reliability** | | | |
| 21 | Alerting On Symptoms Versus Causes | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m05l01) | — | [§](https://learnsome.tech/courses/observability-course/book#lesson-5-1) |
| 22 | Alerting Rules And The For Duration | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m05l02) | — | [§](https://learnsome.tech/courses/observability-course/book#lesson-5-2) |
| 23 | Service Level Indicators | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m05l03) | [labs/m05l03/](labs/m05l03/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-5-3) |
| 24 | Service Level Objectives | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m05l04) | [labs/m05l04/](labs/m05l04/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-5-4) |
| 25 | Error Budgets And Burn Rate Alerts | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m05l05) | [labs/m05l05/](labs/m05l05/) | [§](https://learnsome.tech/courses/observability-course/book#lesson-5-5) |
| | **Incident Response And Postmortems** | | | |
| 26 | On Call And Incident Command | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m06l01) | — | [§](https://learnsome.tech/courses/observability-course/book#lesson-6-1) |
| 27 | The Blameless Postmortem | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m06l02) | — | [§](https://learnsome.tech/courses/observability-course/book#lesson-6-2) |
| 28 | A Worked Example Postmortem | [▶](https://learnsome.tech/courses/observability-course/watch?lesson=m06l03) | — | [§](https://learnsome.tech/courses/observability-course/book#lesson-6-3) |

## Exercises

Each lesson folder contains an `EXERCISES.md` with hands-on tasks drawn directly from the course material.
Open the file for a lesson to see the tasks and, where provided, hints.

---

© LearnSome.tech · support@iwantto.learnsome.tech
