from app.db import get_user


class FakeCursor:
    def __init__(self):
        self.executed = None
        self.params = None

    def execute(self, query, params=None):
        self.executed = query
        self.params = params

    def fetchall(self):
        return [{"id": 1, "name": "alice"}]


def test_get_user_returns_rows():
    # Behaviour is invariant under the fix (string-format -> parameterised),
    # so a correct remediation keeps this green.
    c = FakeCursor()
    assert get_user(c, "1") == [{"id": 1, "name": "alice"}]
    assert c.executed is not None
