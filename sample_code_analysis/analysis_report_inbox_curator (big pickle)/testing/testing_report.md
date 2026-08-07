# Testing Analysis Report — Inbox Curator

> Generated: 2026-08-07 · Toolchain: pytest 9.1.1 + pytest-cov 7.1.0 + coverage 7.15.3 · Python 3.10.0

---

## 1. Summary

| Metric | Value |
|---|---|
| Tests collected / run | 7 |
| Tests passing | 7 (100%) |
| Test runner time | ~0.9 s |
| Framework | `unittest` classes run through `pytest` |
| Overall line coverage | **72%** (665 statements, 186 missed) |
| HTML report | [coverage/index.html](./coverage/index.html) *(open in a browser)* |
| Coverage visuals | [testing_visuals.md](../assets/testing_visuals.md) |

The suite is small, fast, and green, but it covers only the happy paths. Two entry-point modules
(`app.py`, `delete_api.py`) have **0% coverage**, error paths are largely untested, and one test file
(`tests/testfilter.py`) is silently **not executed** by pytest.

---

## 2. Test inventory

| File | Tests | Notes |
|---|---|---|
| `tests/test_email_curator.py` | 1 | Mocks fetcher, filters, Redis; checks orchestrator wiring |
| `tests/test_email_fetcher.py` | 1 | Mocks Graph API response; asserts a single `rpush` |
| `tests/test_email_handlers.py` | 3 | One per handler; mocks HTTP and Redis |
| `tests/test_token_refresher.py` | 1 | Mocks token POST; verifies observer notification |
| `tests/test_stub.py` | 1 | Empty `test_stub()` — no value, should be deleted |
| `tests/testfilter.py` | 3 | **Not collected** by pytest (filename lacks `test_` prefix) |

`pytest.ini`:
```ini
[pytest]
addopts = -v -x --cov=src/ --cov-report=term-missing --import-mode=append
testpaths = tests src
```

---

## 3. Coverage by module

| Module | Coverage | Missed lines (examples) |
|---|---|---|
| `Config/env.py` | 100% | — |
| `Config/redis_config.py` | 100% | — |
| `EmailCurator/EmailCurator.py` | 97% | 72 |
| `EmailFetcher/EmailFetcher.py` | 81% | 41–43, 53–54, 117–119 |
| `EmailFilter/BaseHandler.py` | 75% | 70–72, 90–92 |
| `EmailFilter/BounceHandler.py` | 91% | 52–53, 73 |
| `EmailFilter/DeleteHandler.py` | 67% | 35–39, 47, 68–75, 89–97 |
| `EmailFilter/GroupingHandler.py` | 60% | 115–135, 156–160, 181–188, 197–198 |
| `Scheduler/scheduler.py` | 79% | 63–64, 70–71, 80 |
| `TokenRefresher/TokenRefresher.py` | 76% | 84–89, 110–117, 139–150 |
| `Utilities/getfilters.py` | 38% | 21–29 |
| `Utilities/isotimestamp.py` | 100% | — |
| `Utilities/pathmaker.py` | 100% | — |
| `Utilities/text_processing.py` | 92% | 35 |
| `app.py` | **0%** | whole module |
| `delete_api.py` | **0%** | whole module |
| `logger.py` | 87% | 102–112, 125–141, 225–230 |

### Key gaps

- **`app.py` and `delete_api.py` are completely untested.** `app.py` is the Celery wiring that starts the
  whole service; `delete_api.py` is the Flask endpoint (note: it imports `flask`, which is not in
  `requirements.txt`).
- **`getfilters.py` at 38%** — the failure path of `fetch_filters` (HTTP error → `None`) is untested.
- **`GroupingHandler` at 60%** — the unsubscribe-group branch, negative-keyword logic, default-group
  assignment, and all `except` paths are untested.
- **`DeleteHandler` at 67%** — the "push back to Redis on failure" path and the `delete_email` error branches
  are untested.
- **`TokenRefresher` at 76%** — empty-token and request-failure branches untested.

---

## 4. Test quality findings

### Confirmed issues

1. **`tests/testfilter.py` never runs.** It is not collected because the file name is `testfilter.py`
   (missing `_`), which does not match pytest's `test_*.py` pattern. Worse, its three tests build the real
   handler chain **without mocking HTTP**, so if the file were renamed it would issue live
   `requests.delete`/`requests.post` calls to the real Graph and backend URLs. It should be deleted or
   fully mocked and renamed.

2. **`test_stub.py` is an empty placeholder** (`def test_stub(): pass`). It contributes a false sense of
   coverage and should be removed.

3. **Mock assertions are weak / incorrect in places:**
   - `test_email_handlers.py::TestGroupHandler` mocks `requests.post` but never sets
     `mock_requests_post.return_value.status_code = 201` before `handler.handle(...)` is run; the mock is
     set *after* the call (line 79), so `BaseHandler.response` returns `False`, the handler falls into the
     failure branch and tries to re-push to Redis. The assertion `assert_called_once` still passes, masking
     the fact that the failure path executed.
   - `test_email_curator.py` mocks `DeleteHandler` entirely, so the real chain logic is never exercised.

4. **`pytest.ini` uses `-x` (stop on first failure).** A single regression aborts the whole suite before
   other tests can report, making CI output less informative.

5. **No tests for the Redis batch loop in `EmailCurator`** (pagination/trim behaviour), the off-by-one in
   `ltrim("emails", 99, -1)`, or multi-page fetching in `EmailFetcher`.

6. **No tests for `logger.py`'s colour/file output** or the `set_console_mode`/`set_file_mode` toggles.

### Recommendations

- Delete `test_stub.py` and fix or delete `testfilter.py`.
- Add unit tests for `app.py` (task wiring) and `delete_api.py` (auth key check, missing payload, success).
- Add failure-path tests: `fetch_filters` returning `None` on HTTP error; token refresh returning empty
  tokens; Graph API errors; `DeleteHandler` returning `False` → re-queue behaviour.
- Add edge-case tests: emails with fractional-second `receivedDateTime`, missing `internetMessageHeaders`,
  `toRecipients` with no `<`/`>`, non-dict entries in the Redis list.
- Use `responses` or `requests_mock` for HTTP mocking instead of `unittest.mock.patch` per module.
- Drop `-x` from `addopts` (or keep it only locally) so CI reports all failures.
- Consider a coverage gate (e.g. `--cov-fail-under=75`) to prevent regressions.

---

## 5. Artifacts

- HTML coverage report: [coverage/index.html](./coverage/index.html)
- Coverage visualizations: [../assets/testing_visuals.md](../assets/testing_visuals.md)
- Raw run: 7 passed in 0.92s
