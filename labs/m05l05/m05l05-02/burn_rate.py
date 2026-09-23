# Full-Stack Observability: Metrics, Tracing & Logging — lesson m05l05 — Error Budgets And Burn Rate Alerts
# https://learnsome.tech/courses/observability-course/watch?lesson=m05l05
# © LearnSome.tech

print(f"objective {conf['objective']}, error budget {round(budget, 4)}")
print(f"{'window':>8} {'errors':>8} {'requests':>9} {'ratio':>8} {'burn':>7}")
for window in windows:
    ratio = window["errors"] / window["requests"]
    burn = ratio / budget
    print(f"{window['window']:>8} {window['errors']:>8} "
          f"{window['requests']:>9} {round(ratio, 5):>8} {round(burn, 1):>7}")

fast = {w["window"]: w["errors"] / w["requests"] / budget for w in windows}
page = (fast.get("1h", 0) > conf["page_burn_rate"]
        and fast.get("5m", 0) > conf["page_burn_rate"])
ticket = fast.get("6h", 0) > conf["ticket_burn_rate"]
print("page:", "yes" if page else "no")
print("ticket:", "yes" if ticket else "no")
