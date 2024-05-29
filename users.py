# the commented out code is the code that should be used in the secure version
# import secrets
from flask import session, abort, request
# from werkzeug.security import check_password_hash, generate_password_hash
from db_connection import get_db

def register(username, password, role):
    # hash_value = generate_password_hash(password)
    connection = get_db()
    cur = connection.cursor()
    try:
        sql = """INSERT INTO users (username, password, role)
                 VALUES (?, ?, ?)"""
        cur.execute(
            sql, [username, password, role])
            # instead of the clear text password variable, should use hash_value
        connection.commit()
    except:
        return False
    return login(username, password)


def login(username, password):
    connection = get_db()
    cur = connection.cursor()

    #sql = "SELECT * FROM users WHERE username = ?"
    #result = cur.execute(sql, [username])

    sql = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    result = cur.execute(sql)

    user = result.fetchone()

    if user is None:
        return False
    #if not check_password_hash(user[2], password):
    #    return False

    session["user_id"] = user['id']
    session["username"] = user['username']
    session["user_role"] = user['role']
    # session["csrf_token"] = secrets.token_hex(16) #<- This should be done
    # because assigning an unique token for each session is a good practice
    # to prevent CSRF attacks.

    return True


def logout():
    del session["user_id"]
    del session["username"]
    del session["user_role"]
    #del session["csrf_token"]

def get_current_user():
    return [session["user_id"], session["username"], session["user_role"]]

def get_users():
    connection = get_db()
    cur = connection.cursor()
    sql = "SELECT id, username, role FROM users"
    result = cur.execute(sql)
    users = result.fetchall()
    return users

def get_user(user_id):
    connection = get_db()
    cur = connection.cursor()
    sql = "SELECT id, username, role FROM users WHERE id=?"
    result = cur.execute(sql, [user_id])
    user = result.fetchone()
    return user

def update_role(user_id, role):
    connection = get_db()
    cur = connection.cursor()
    sql = "UPDATE users SET role=? WHERE id=?"
    cur.execute(sql, [role, user_id])
    connection.commit()
    return True

def remove_user(user_id):
    connection = get_db()
    cur = connection.cursor()

    sql = "DELETE FROM users WHERE id=?"
    cur.execute(sql, [user_id])
    connection.commit()
    
    return True

def require_role(): # this should be used in the routes that require admin role
    if  session["user_role"] != "admin":
        abort(403)


def check_csrf(): # this should be used in the routes that require csrf token
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)