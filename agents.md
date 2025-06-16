# Agent Work Instructions
Find the first unchecked item in **todo.md** and:

1. Add wrapper(s) in **`openphone_sdk/`**
2. Re-export in **`openphone_sdk/__init__.py`**
3. Add a **Pytest** test under **`tests/`**
4. Mark the task complete (`[x]`)
5. Run `pytest` locally; open the PR only if tests pass

## Coding conventions
* Import the shared helper `client()` from `openphone_sdk.request` – **never** create your own `AuthenticatedClient`.
* Place all functions for the same path in a single module (`openphone_sdk/<name>.py`).
* Map 1:1 to *happy-path* return types – raise on any non-200 status.
* Use snake_case filenames: collection → `contacts.py`, single-item (`{id}`) → `contacts_by_id.py`.

## Testing
* Use **pytest-httpx** (`httpx_mock`) to stub requests.
* Verify URL, method, `X-API-KEY` header, and any JSON body.
* Tests must pass with `pytest -q`.

## CI expectation
A PR is merge-ready only if `pytest` exits with status 0.
