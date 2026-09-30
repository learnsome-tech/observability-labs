# m01l03 · Structured Logging And Why Text Fails

Module 1: The Foundations Of Observability · lesson 1.3 · Free · [Open the lesson](https://learnsome.tech/learn/observability-course/m01l03)

**Goal:** You can write log events as records with stable field names, explain why a sentence is not a log, and query your own logs without a regular expression.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l03-02](m01l03-02/) | The same three events, written as prose | Graded |
| [m01l03-03](m01l03-03/) | The same three events, written as records | Graded |
| [m01l03-04](m01l03-04/) | Now a question is a query, not a regular expression | Graded |
| [m01l03-05](m01l03-05/) | The logger the service in this course uses | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn

1. Add a field for the payment method to the order accepted record
2. Write the query that counts accepted orders by that new field
3. Now rename the field and notice exactly what your query returns

> **Hint:** The third step is the point of the exercise, not an accident.

## Check yourself

- Why does a prose log line resist filtering and counting?
- What breaks when somebody changes the wording of a log message?
- What happens to saved queries when a field is renamed, and what is the warning?
- Which two things must never appear in a log line?
- Which field lets you move from a log record to the request it belongs to?

---

[Course README](../../README.md) · [Full-Stack Observability: Metrics, Tracing & Logging on LearnSome.tech](https://learnsome.tech/courses/observability-course)
