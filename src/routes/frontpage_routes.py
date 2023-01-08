from app import app
from flask import redirect

@app.route("/")
def index():
    return redirect("/forums")
