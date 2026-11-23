"""Tiny user lookup — contains a deliberate SQL-injection bug for the vh-fixer smoke."""


def get_user(cursor, user_id):
    # Parameterised query: the driver binds user_id safely (no string interpolation).
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchall()
