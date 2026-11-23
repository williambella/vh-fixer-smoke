# vh-fixer-smoke

Throwaway fixture for the **vh-fixer** F1 end-to-end smoke test. `app/db.py` has a
deliberate SQL-injection bug; the governed engine opens a PR that parameterises it.
