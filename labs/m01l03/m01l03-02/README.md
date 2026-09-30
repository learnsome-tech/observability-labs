# m01l03-02 · The same three events, written as prose

**Lesson:** [Structured Logging And Why Text Fails](https://learnsome.tech/learn/observability-course/m01l03) (lesson 1.3, module 1: The Foundations Of Observability) · Free  
**Check:** Graded

## Goal

You can write log events as records with stable field names, explain why a sentence is not a log, and query your own logs without a regular expression.

In the lesson: Here are three events written the way most services write them. Run it and you get three perfectly readable lines. A person can read those. Now try to answer a question with them: how much money did these accepted orders come to? The amount is in there, somewhere after the word totalling, mixed in with a user identifier that also happens to contain digits. You would write a regular expression, get it slightly wrong, and never know. Then somebody changes the wording to reads was accepted successfully, and every query built on the old wording quietly returns nothing at all. Nothing failed. There is just no result, which is worse.

## Files

- [`starter/text_log.py`](starter/text_log.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-02/starter`
2. Read `text_log.py`.
3. Run it: `python3 text_log.py`.
4. Check it from the repository root: `./check m01l03-02`.

## Expected output

```text
09:41:02 checkout: order 1071 for user u4 totalling 31.86 pounds was accepted
09:41:02 checkout: order 1072 for user u1 totalling 74.63 pounds was accepted
09:41:02 checkout: order 1073 for user u4 totalling 8.5 pounds was accepted
```

## How to check

`./check m01l03-02` copies `starter/` into a scratch directory and runs `python3 text_log.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/observability-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
