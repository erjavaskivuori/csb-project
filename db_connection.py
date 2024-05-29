import os
import sqlite3
from flask import g

database = os.getenv('DATABASE')

def get_db():
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    connection = sqlite3.connect(database)
    cur = connection.cursor()

    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("DROP TABLE IF EXISTS messages")

    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur.execute("""INSERT INTO users (username, password, role) 
                VALUES ('admin', 'admin', 'admin');""")

    connection.commit()
    connection.close()

if __name__ == '__main__':
    init_db()