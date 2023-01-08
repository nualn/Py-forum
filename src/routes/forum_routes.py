from flask import render_template, request, redirect

from app import app
from controllers import users, forums

@app.route("/forums", methods=["GET", "POST"])
def forums_handler():
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
    
    return render_template("error.html", message="Invalid request method")

@app.route("/forums/<int:forum_id>", methods=["DELETE", "PUT"])
def forum(forum_id):
    users.check_csrf()
    users.check_admin()

    if request.method == "DELETE":
        if forums.delete_forum(forum_id):
            return redirect("/forums")
        return render_template("error.html", message="Forum deletion failed")

    if request.method == "PUT":
        name = request.form["name"]
        description = request.form["description"]
        if forums.update_forum(forum_id, name, description):
            return redirect("/forums")
        return render_template("error.html", message="Forum update failed")
