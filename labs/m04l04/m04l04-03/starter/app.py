        started = time.monotonic()
        inflight.add(1)
        incoming = tracing.parse_traceparent(self.headers.get("traceparent"))
        trace_id = incoming[0] if incoming else tracing.new_trace_id()
        span = tracing.Span("GET " + route, trace_id, tracing.new_span_id(),
                            incoming[1] if incoming else None)
        status, payload = work(route)
        elapsed = time.monotonic() - started
        span.set("http.route", route)
        span.set("http.response.status_code", status)
        span.end("ERROR" if status >= 500 else "OK")
        tracing.export([span])
        requests_total.inc(method="GET", route=route, status=status)
        request_seconds.observe(elapsed, route=route)
        inflight.add(-1)
        log("ERROR" if status >= 500 else "INFO", "http_request",
            route=route, status=status, duration_ms=round(elapsed * 1000, 1),
            trace_id=trace_id)
        self.send_body(status, json.dumps(payload) + "\n", "application/json")
