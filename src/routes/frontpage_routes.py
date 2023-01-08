from flask import redirect
from app import app

@app.route("/")
def index():
    return redirect("/forums")
