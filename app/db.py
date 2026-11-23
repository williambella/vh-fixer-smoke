"""Tiny user lookup — contains a deliberate SQL-injection bug for the vh-fixer smoke."""


def get_user(cursor, user_id):
    # BUG (synthetic): SQL injection via string interpolation of untrusted input.
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cursor.execute(query)
    return cursor.fetchall()
