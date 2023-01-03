from app import app
from flask import render_template, request, redirect
from controllers import users, forums

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