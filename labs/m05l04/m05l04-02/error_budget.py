# Full-Stack Observability: Metrics, Tracing & Logging — lesson m05l04 — Service Level Objectives
# https://learnsome.tech/courses/observability-course/watch?lesson=m05l04
# © LearnSome.tech
total = sum(d["total"] for d in days)
errors = sum(d["errors"] for d in days)
budget = total * (1 - conf["objective"])
used = errors / budget
elapsed = len(days)

print("objective:", conf["objective"])
print("requests:", total)
print("allowed failures:", round(budget, 1))
print("actual failures:", errors)
print("budget used:", f"{round(used * 100, 1)} per cent")
print("budget left:", f"{round((1 - used) * 100, 1)} per cent")
print("days elapsed:", elapsed)
if errors:
    rate = errors / elapsed
    print("days to exhaustion:", round((budget - errors) / rate, 1))
