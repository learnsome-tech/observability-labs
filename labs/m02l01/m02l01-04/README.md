# m02l01-04 · Why a counter is useless until you ask about time

**Lesson:** [Metric Types: Counters And Gauges](https://learnsome.tech/learn/observability-course/m02l01) (lesson 2.1, module 2: Metrics And Prometheus) · Pro  
**Check:** Graded

## Goal

You can choose between a counter and a gauge for any measurement, name them the way Prometheus expects, and explain why a counter is only useful once you take its rate.

In the lesson: The raw value of a counter is an accident of how long the process has been running, so nobody looks at it. What you want is how fast it is going up. Here are five samples taken fifteen seconds apart, and notice the fourth: the value collapses, because the process restarted. Subtracting the first from the last gives a negative number, which is obvious nonsense. The fix is to walk the samples and treat a fall as a restart, adding the new value rather than the difference. Run the arithmetic and you get ninety five over sixty seconds. Prometheus does exactly this for you, and it is why you take the rate of a counter instead of reading it.

## Files

- [`starter/counters.py`](starter/counters.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-04/starter`
2. Read `counters.py` the way the lesson builds it:
   - Lines 1–3: five samples
   - Lines 4–11: treat a fall as a restart
   - Lines 12–18: run the arithmetic
3. Run it: `python3 counters.py`.
4. Check it from the repository root: `./check m02l01-04`.

## Expected output

```text
raw difference: -65
increase with reset handling: 95.0
seconds: 60
per second: 1.5833
```

## How to check

`./check m02l01-04` copies `starter/` into a scratch directory and runs `python3 counters.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
