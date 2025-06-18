import sqlite3
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

def create_table():
    text = """CREATE TABLE IF NOT EXISTS user(
    telegram_id INT UNIQUE,
    full_name VARCHAT(255),
    user_link TEXT
    );"""
    cursor.execute(text)

def add_user(telegram_id,full_name,user_link):
    text = f"""INSERT INTO user VALUES (
    '{telegram_id}',
    '{full_name}',
    '{user_link}'
    );"""
    cursor.execute(text)
    connection.commit()

def select_user(telegram_id):
    text = f"""SELECT * FROM user WHERE telegram_id='{telegram_id}'"""
    user = cursor.execute(text).fetchone()
    return user

def count_user():
    text = f"""SELECT count() FROM user"""
    return cursor.execute(text).fetchone()[0]

def select_all_users_id():
    text = f"""SELECT telegram_id FROM user"""
    return cursor.execute(text).fetchall()