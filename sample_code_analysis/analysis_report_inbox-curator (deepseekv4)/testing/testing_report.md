# Testing Analysis Report — Inbox Curator

> Generated: 2026-08-07
> HTML Coverage Report: [coverage.html](./coverage.html) *(open in a browser)*
> Coverage Chart: [../assets/coverage_chart.svg](../assets/coverage_chart.svg)

---

## 1. Test Strategy Overview

The project uses **pytest** (configured via `pytest.ini`) with `unittest.TestCase`-style classes and `unittest.mock`. The `Makefile` `test` target first runs `flake8` linting, then `pytest`, then generates an HTML coverage report with `coverage html`.

Test configuration (`pytest.ini`):

```ini
[pytest]
addopts = -v -x --cov=src/ --cov-report=term-missing --import-mode=append
testpaths = tests src
```

### Test Inventory

| Test file | Component under test | Style |
|---|---|---|
| `tests/test_email_curator.py` | `EmailCurator` pipeline orchestration | unittest + mock |
| `tests/test_email_fetcher.py` | `EmailFetch` fetch + Redis store | unittest + mock |
| `tests/test_email_handlers.py` | `DeleteHandler`, `BounceHandler`, `GroupHandler` | unittest + mock |
| `tests/test_token_refresher.py` | `TokenRefresh` refresh + observer notify | unittest + mock |
| `tests/test_stub.py` | Placeholder (empty `test_stub`) | pytest |
| `tests/testfilter.py` | Chain integration (scratch / legacy) | unittest (not collected) |

### Execution Results

```
7 passed in 0.63s
```

All 7 collected tests pass against the current codebase. Note that `tests/testfilter.py` is **not collected** because it does not follow the `test_*.py` / `*_test.py` naming convention.

---

## 2. Coverage Assessment

**Overall statement coverage: 72%** (665 statements, 186 uncovered).

| Module | Stmts | Miss | Cover | Notes |
|---|---|---|---|---|
| `Config/env.py` | 26 | 0 | 100% | Settings singleton |
| `Config/redis_config.py` | 2 | 0 | 100% | Bare client init |
| `EmailCurator/EmailCurator.py` | 36 | 1 | 97% | Misses log line only |
| `Utilities/isotimestamp.py` | 6 | 0 | 100% | |
| `Utilities/pathmaker.py` | 7 | 0 | 100% | |
| `Utilities/text_processing.py` | 13 | 1 | 92% | `strip` edge |
| `EmailFilter/BounceHandler.py` | 45 | 4 | 91% | Missing body-email + retry paths |
| `EmailFilter/BaseHandler.py` | 32 | 8 | 75% | Error branches untested |
| `EmailFilter/DeleteHandler.py` | 57 | 19 | 67% | Error/no-ID/API-failure paths |
| `EmailFetcher/EmailFetcher.py` | 70 | 13 | 81% | Pagination, no-token, HTTP errors |
| `TokenRefresher/TokenRefresher.py` | 82 | 20 | 76% | File-missing, empty-token, notify failure |
| `EmailFilter/GroupingHandler.py` | 107 | 43 | 60% | Negative keywords, unsubscribe, default group |
| `Scheduler/scheduler.py` | 34 | 7 | 79% | Validation + crontab branch |
| `Utilities/getfilters.py` | 13 | 8 | 38% | Entire success path untested |
| `logger.py` | 84 | 11 | 87% | Wrapper methods |
| `app.py` | 22 | 22 | 0% | Entry point never imported |
| `delete_api.py` | 29 | 29 | 0% | Flask API never imported (also not runnable — `flask` missing) |
| **TOTAL** | **665** | **186** | **72%** | |

Key gaps:

- **`app.py` (0%)** — the Celery entry point is never imported or exercised.
- **`delete_api.py` (0%)** — the Flask endpoint has no tests, and `flask` is not in `requirements.txt` so the module cannot even be imported in a fresh environment.
- **`getfilters.py` (38%)** — the happy path (successful GET + JSON parse) is completely untested; only the exception handler is covered indirectly.
- **`GroupingHandler` (60%)** — the unsubscribe-group logic, negative-keyword exclusions, and default-group assignment are untested.
- **`EmailFetcher` pagination, no-token, and HTTP-error branches are untested.**

---

## 3. Test Quality Issues

### 3.1 Faulty assertions / broken tests hidden by mocks

- **`test_email_handlers.py::TestGroupHandler`** patches `src.EmailFilter.BaseHandler.requests.post` and asserts it was called, but never simulates the `response` method's status check beyond setting `mock_requests_post.return_value.status_code = 201`. The success path is only partially verified.
- **`test_email_curator.py`** patches only `DeleteHandler`; the real chain `DeleteHandler(BounceHandler(GroupHandler()))` is not constructed. This verifies the loop plumbing but **not** the handler wiring.
- **`test_email_handlers.py::TestDeleteHandler`** sets `handler.access_token = 'test_token'` manually, which masks the real bug that `DeleteHandler` never initializes `access_token` (see main report, Bug 2).

### 3.2 Fragile environment coupling

- **`test_token_refresher.py`** patches `pickle.dump`/`pickle.load` but **not** `open()`. `Tokens.save_tokens()` will try to open the real `config/tokens.pkl`. If the file or directory is missing (e.g., fresh CI checkout), the test fails. This makes the test environment-dependent.
- Tests import `src.Config.env.app_env` (in `test_email_handlers.py`), which requires a populated `config/.env` file to be present. CI without `.env` will fail at collection time.
- `test_email_handlers.py::TestDeleteHandler` builds the expected URL from `app_env.delete_base_url`, coupling the test to environment configuration.

### 3.3 Naming / organization

- `tests/testfilter.py` is a legacy scratch file. Its assertions reference behavior that no longer exists (`delete_handler.handle(email, ...)` returns strings like `"Email deleted successfully"`, but the current code returns `None`/`True`). **These tests would fail if collected.** It is not collected only because of the filename convention. It should be deleted or rewritten.
- `tests/test_stub.py` is a meaningless placeholder and should be removed.
- Tests use `unittest` classes instead of plain pytest functions/fixtures, but `pytest.ini` adds `-x` (stop at first failure) and coverage flags — reasonable, but `-x` can hide later failures in the suite.

### 3.4 Lint failures in tests

Running the project's `flake8` (max-line-length 120) over `tests/` reports multiple violations (E302 blank lines, E501 long lines, W291/W293 whitespace, W292 missing newline at EOF, F401 unused import in `test_email_curator.py`). The `Makefile` lint target only covers `src/`, so these go uncaught by CI.

---

## 4. Missing Tests / Recommended Test Cases

| Priority | Area | Test case |
|---|---|---|
| High | `EmailCurator` | `fetch_filters()` returns `None` → task must not crash with `TypeError` |
| High | `DeleteHandler` | `delete_email()` called when `access_token` is unset → graceful `False`, no `AttributeError` |
| High | `DeleteHandler` | `email["email_id"] is None` and `email["from"] is None` are skipped |
| High | `EmailFetcher` | No `access_token` set → raises `ValueError` |
| High | `EmailFetcher` | Paginated response with `@odata.nextLink` → multiple pages fetched |
| High | `EmailFetcher` | Graph API returns non-200 / connection error → handled gracefully |
| High | `BounceHandler` | No email found in bounce body → `from` set safely, no crash |
| High | `BounceHandler` | POST failure → only the bounced emails re-queued, not the full batch |
| High | `GroupHandler` | Negative keyword excludes a positive match |
| High | `GroupHandler` | Unsubscribe group matched before other groups; default group fallback |
| Medium | `TokenRefresher` | `tokens.pkl` missing / empty → handled without crash |
| Medium | `TokenRefresher` | Observer `update()` raises → other observers still notified |
| Medium | `getfilters` | Successful GET returns parsed JSON |
| Medium | `logger` | Level filtering console vs file; file/line info capture |
| Medium | `app.py` | Import succeeds; Celery tasks registered with correct names |
| Medium | `delete_api.py` | Missing/invalid API key → 403; valid payload → 200; handler exception → 500 |
| Low | `isotimestamp` | Fractional-seconds and timezone-offset timestamps parse correctly |
| Low | `scheduler` | `register_task` adds beat schedule entry; invalid `task_name` raises `ValueError` |

---

## 5. Recommendations

1. **Delete `tests/testfilter.py` and `tests/test_stub.py`** — they are stale or meaningless and `testfilter.py` encodes out-of-date behavior.
2. **Decouple tests from the environment**: patch `open()` in token tests, provide a fixture `.env`/test settings, and avoid depending on real `app_env` values.
3. **Add the high-priority edge-case tests** in the table above — most target confirmed bugs in the main report.
4. **Import `app.py` in a smoke test** so the 0%-coverage entry point is at least verified to load and register tasks.
5. **Add `delete_api.py` tests** once `flask` is added to `requirements.txt`.
6. **Lint `tests/` as well** (extend the Makefile `lint` target or CI job) so style issues are caught.
7. Consider switching to plain pytest fixtures and removing `-x` so all failures surface in one run.
8. Use a `conftest.py` fixture to reset mocked singletons (e.g., `JSJD_logger`, `Settings`) between tests to avoid cross-test state leakage.

---

## 6. Artifacts

- **HTML coverage report:** [coverage.html](./coverage.html)
- **Coverage by module chart:** [../assets/coverage_chart.svg](../assets/coverage_chart.svg)
