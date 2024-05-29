# the commented out code is the code that should be used in the secure version
import os
from string import printable
from flask import Flask, render_template, request, redirect, url_for, session, abort
import users
import messages

app = Flask(__name__)
app.secret_key = 'very_secret_key'
# app.secret_key = os.getenv('SECRET_KEY')

@app.route("/")
def index():
    all_messages = messages.get_messages()
    return render_template("index.html", messages=all_messages)

@app.route("/send", methods=["POST"])
def send():
    # users.check_csrf() <- This should be done to prevent CSRF attacks
    user_id = users.get_current_user()[0]
    message = request.form["message"]

    if len(message) > 200:
        error = "Message is too long."
        return render_template("index.html", error=error)
    
    messages.send_message(user_id, message)
    return redirect(url_for('index'))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not users.login(username, password):
            error = "Wrong credentials!"
            return render_template("login.html", error=error)

    return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) > 20:
            error = "Username can't be longer than 20 characters."
            return render_template("register.html", error=error)

        for i in username:
            if i not in printable and i != " ":
                error = """Password can only contain letters a-z, A-Z,
                numbers and special characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
                return render_template("register.html", error=error)

        password = request.form["password"]
        if len(password) < 8:
            error = "Password must be at least 8 characters long."
            return render_template("register.html", error=error)
        if len(password) > 50:
            error = "Password can't be longer than 50 characters."
            return render_template("register.html", error=error)
        for i in password:
            if i not in printable and i != " ":
                error = """Password can only contain letters a-z, A-Z,
                numbers and special characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
                return render_template("register.html", error=error)

        role = "user"

        if users.register(username, password, role):
            return redirect("/")
            
    return render_template("register.html", error="Registration was unsuccessful.")

@app.route("/users/<int:id>")
def user(id):
    # admin = (session["user_role"] == "admin")
    # own_profile = (id == session["user_id"])
    
    #if not admin or not own_profile:
    #    abort(403)

    user = users.get_user(id)
    return render_template("user.html", user=user)

@app.route("/admin")
def admin():
    #users.require_role()

    all_users = users.get_users()
    return render_template("admin.html", users=all_users)

@app.route("/editrole", methods=["POST"])
def edit_role():
    # users.require_role()
    # users.check_csrf() <- This should be done to prevent CSRF attacks

    user_id = request.form["user_id"]
    new_role = request.form["role"]
    users.update_role(user_id, new_role)
    return redirect("/admin")

@app.route("/deleteuser", methods=["POST"])
def delete_user():
    user_id = request.form["user_id"]
    # users.check_csrf() <- This should be done to prevent CSRF attacks

    admin = (session["user_role"] == "admin")
    own_profile = (user_id == session["user_id"])
    if not admin or not own_profile:
        abort(403)

    users.remove_user(user_id)
    return redirect("/admin")