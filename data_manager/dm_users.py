from connection import connection_handler


@connection_handler
def get_users(cursor):
    cursor.execute("""
                    SELECT * FROM users
                    """)
    users = cursor.fetchall()
    return users


@connection_handler
def get_user(cursor, user_id):
    cursor.execute("""
                    SELECT * FROM users
                    WHERE id=%(id)s
                    """,
                   {'id': user_id})
    user = cursor.fetchone()
    return user


@connection_handler
def get_user_questions(cursor, user_id):
    cursor.execute("""
                    SELECT * FROM question
                    WHERE users_id=%(id)s
                    """,
                   {'id': user_id})
    questions = cursor.fetchall()
    return questions


@connection_handler
def get_user_answers(cursor, user_id):
    cursor.execute("""
                    SELECT * FROM answer
                    WHERE users_id=%(id)s
                    """,
                   {'id': user_id})
    answers = cursor.fetchall()
    return answers


@connection_handler
def get_user_comments(cursor, user_id):
    cursor.execute("""
                    SELECT * FROM comment
                    WHERE users_id=%(id)s
                    """,
                   {'id': user_id})
    comments = cursor.fetchall()
    return comments


@connection_handler
def get_users_sorted(cursor, order_by, order_direction):
    cursor.execute(f"""
                    SELECT * FROM users ORDER BY {order_by} {order_direction}
                    """)
    users = cursor.fetchall()
    return users
