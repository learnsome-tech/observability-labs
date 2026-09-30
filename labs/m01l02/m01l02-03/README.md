# m01l02-03 · A log: one record per event, full of detail

**Lesson:** [The Three Signals: Logs, Metrics And Traces](https://learnsome.tech/learn/observability-course/m01l02) (lesson 1.2, module 1: The Foundations Of Observability) · Free  
**Check:** Graded

## Goal

You can say what a log, a metric and a trace each answer well, what each costs, and which one to reach for when something is wrong.

In the lesson: Now a log. Three orders, three records, and each one keeps the detail the counter threw away: which order, how much money, which user. That is the opposite bargain. A log grows in step with traffic, so the cost is real, and at high volume teams start sampling or dropping them. In exchange you can answer questions about one specific event, which is exactly what you need when a named customer is on the phone. Notice these are written as data rather than as English sentences. That single decision is the difference between a log you can query and a log you can only read, and the next lesson is about nothing else.

## Files

- [`starter/json_log.py`](starter/json_log.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-03/starter`
2. Read `json_log.py`.
3. Run it: `python3 json_log.py`.
4. Check it from the repository root: `./check m01l02-03`.

## Expected output

```text
{"event": "order_accepted", "order_id": 1071, "total_gbp": 31.86, "user_id": "u4"}
{"event": "order_accepted", "order_id": 1072, "total_gbp": 74.63, "user_id": "u1"}
{"event": "order_accepted", "order_id": 1073, "total_gbp": 8.5, "user_id": "u4"}
```

## How to check

`./check m01l02-03` copies `starter/` into a scratch directory and runs `python3 json_log.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
