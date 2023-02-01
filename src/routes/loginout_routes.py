from app import app
from flask import request, redirect, render_template
from controllers import users

@app.route("/login", methods=["GET", "POST"])
def login_handler():
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
def register_handler():
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
def logout_handler():
    users.logout()
    return redirect("/")