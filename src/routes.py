from flask import render_template, request, session, redirect, abort
from controllers import users, forums
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Invalid username or password")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords do not match")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Registration failed")
            
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/forums", methods=["GET", "POST"])
def show_forums():
    if request.method == "GET":
        forums_list = forums.get_forums()
        return render_template("forums.html", forums=forums_list)
    if request.method == "POST":
        users.check_csrf()
        users.check_admin()
        name = request.form["name"]
        description = request.form["description"]
        if forums.create_forum(name, description):
            return redirect("/forums")
        else:
            return render_template("error.html", message="Forum creation failed")

@app.route("/forums/<int:forum_id>", methods=["DELETE", "PUT"])
def forum(forum_id):
    if request.method == "DELETE":
        users.check_csrf()
        users.check_admin()
        if forums.delete_forum(forum_id):
            return redirect("/forums")
        else:
            return render_template("error.html", message="Forum deletion failed")

    if request.method == "PUT":
        users.check_csrf()
        users.check_admin()
        name = request.form["name"]
        description = request.form["description"]
        if forums.update_forum(forum_id, name, description):
            return redirect("/forums")
        else:
            return render_template("error.html", message="Forum update failed")
