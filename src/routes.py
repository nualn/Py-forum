from flask import render_template, request, session, redirect
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")