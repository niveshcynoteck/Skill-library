# Testing Analysis — Inbox Curator

> **Generated:** 2026-08-07
> **HTML coverage report:** [coverage.html](./coverage.html) *(open in a browser)*
> **Coverage chart:** [../assets/coverage.png](../assets/coverage.png)

---

## 1. Test Suite Overview

| Metric | Value |
|---|---|
| Test files | 6 (`tests/test_email_curator.py`, `test_email_fetcher.py`, `test_email_handlers.py`, `test_token_refresher.py`, `test_stub.py`, `testfilter.py`) |
| Tests collected by pytest | **7** (all pass) |
| Tests silently skipped | **3** in `tests/testfilter.py` (filename does not match `test_*.py`) |
| Framework | `unittest` classes run under `pytest` (`pytest.ini` sets `--import-mode=append`) |
| Coverage | **72%** overall (665 statements, 186 missed) |
| Coverage tooling | `pytest-cov` + `coverage.py`, HTML report generated |

The collected suite is small but healthy: 7 tests, all passing, using mocking to isolate
external dependencies (Redis, `requests`, `pickle`). This is a good foundation, but coverage is
uneven and several important modules and code paths are not exercised at all.

## 2. Test Quality

**Strengths**

- Dependencies are mocked (Redis client, HTTP calls, token file), so the suite runs fast
  (~0.5 s) and deterministically without external services.
- Tests are readable and each targets one handler or task.
- Mocking is applied at the correct namespace (e.g. `src.EmailCurator.EmailCurator.redis_client`).

**Weaknesses**

- **`tests/testfilter.py` is never collected.** The file is named `testfilter.py`, which does not
  match pytest's `test_*.py` pattern, so its 3 tests never run. Worse, those tests are **out of
  date**: they were written for an older single-email API and all 3 fail when run manually:
  - They expect string return values (`"Email deleted successfully"`, `"Email grouped
    successfully"`) but `handle()` returns `None`.
  - They pass a **single email dict**, while the handlers now expect a **list** of emails.
  - They pass `emailsToRemove` as a list of strings, while `DeleteHandler` expects
    `[{"email_address": ...}]`.
  → This file should be either deleted or rewritten to match the current list-based API.
- `tests/test_stub.py` is an empty placeholder (`def test_stub(): pass`) and should be removed.
- No tests exist for `src/app.py`, `src/delete_api.py`, `src/logger.py`, `src/Utilities/*`,
  or `src/Scheduler/scheduler.py`.
- Minor style violations (unused import `MagicMock` in `test_email_curator.py`, missing blank
  lines, line-too-long) fail `flake8` when run against `tests/` — though the Makefile only lints
  `src/`.

## 3. Coverage Assessment

Overall coverage is **72%**, but it is very uneven:

| Module | Coverage | Notes |
|---|---|---|
| `src/app.py` | **0%** | Entry point — never imported by tests |
| `src/delete_api.py` | **0%** | Flask endpoint — never imported (also `flask` not installed) |
| `src/Utilities/getfilters.py` | **38%** | Only success path partially covered |
| `src/EmailFilter/GroupingHandler.py` | **60%** | Unsubscribe logic, negative keywords uncovered |
| `src/EmailFilter/DeleteHandler.py` | **67%** | Failure/retry paths uncovered |
| `src/EmailFilter/BaseHandler.py` | **75%** | `response()` error paths uncovered |
| `src/Scheduler/scheduler.py` | **79%** | `register_task`/crontab uncovered |
| `src/TokenRefresher/TokenRefresher.py` | **76%** | Failure paths uncovered |
| `src/EmailFetcher/EmailFetcher.py` | **81%** | Pagination/error paths uncovered |
| `src/logger.py` | **87%** | Setter bugs untested |
| `src/EmailFilter/BounceHandler.py` | **91%** | Push-back path uncovered |
| `src/EmailCurator/EmailCurator.py` | **97%** | Good |

> The 3 modules at **0%** are the application's entry points — the glue between Celery, the
> token refresh, and the pipeline — and the Flask deletion API. These are the most valuable
> modules to cover next.

## 4. Recommendations

1. **Fix or remove `tests/testfilter.py`.** Rename it to `test_filter.py` and rewrite the tests
   for the current list-based handler API, or delete it. Leaving it silently failing is the
   worst option.
2. **Remove `tests/test_stub.py`.**
3. **Add entry-point tests** for `src/app.py` (mock `TokenRefresh`, `EmailCurator`, Celery) and
   `src/delete_api.py` (mock Flask request + token + `DeleteHandler`).
4. **Add unit tests for `src/logger.py`**, including the `set_console_mode(False)` bug (it
   currently does not disable console output).
5. **Add tests for failure/retry paths:**
   - `DeleteHandler` — `requests.delete` returns non-204 → email pushed back to Redis.
   - `BounceHandler` — `response()` returns False → full-list push-back branch.
   - `GroupHandler` — negative keywords, unsubscribe group, default group, malformed group data.
   - `TokenRefresh` — token endpoint failure, empty tokens.
   - `EmailFetcher` — pagination via `@odata.nextLink`, missing access token, HTTP error.
6. **Add tests for the Redis batch loop** in `EmailCurator` (this is where the `ltrim` off-by-one
   produces duplicates — a regression test with >100 emails would catch it).
7. **Test edge cases in `Utilities`:**
   - `subtract_hours_from_iso` with fractional seconds / timezone offsets (currently crashes).
   - `text_normalization` with links, unicode, and whitespace.
8. **Use a coverage gate.** Add `--cov-fail-under=80` to `pytest.ini` addopts so coverage cannot
   regress silently, then aim for 90%+.
9. **Declare dev dependencies** (`pytest`, `pytest-cov`, `coverage`, `flake8`) in a
   `requirements-dev.txt` so CI and contributors install the test toolchain.
10. **Lint tests too.** Extend `make lint` to run `flake8` on `tests/` as well as `src/`.

## 5. Suggested Additional Test Cases

- `DeleteHandler` with a `None` `email_id` (current guard is a no-op — see main report).
- `DeleteHandler` receiving a single dict instead of a list (contract mismatch).
- `BounceHandler`/`GroupHandler` push-back: assert each email is pushed **individually**, not the
  whole list as one JSON entry (current behaviour corrupts the queue).
- `EmailCurator` with `fetch_filters()` returning `None` (currently raises `TypeError`).
- `EmailCurator` batch loop with 101+ emails to catch the duplicate-processing bug.
- API-key auth on `delete_api.py`, including the wrong-key path and constant-time comparison.
