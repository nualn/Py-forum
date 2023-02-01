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
        return render_template("error.html", message="Forum creation failed")

    return render_template("error.html", message="Invalid request method")

@app.route("/forums/<int:forum_id>/delete", methods=["POST"])
def forum_delete_handler(forum_id):
    users.check_csrf()
    users.check_admin()

    if forums.delete_forum(forum_id):
        return redirect("/forums")
    return render_template("error.html", message="Forum deletion failed")

@app.route("/forums/<int:forum_id>/edit", methods=["GET", "POST"])
def forum_edit_handler(forum_id):
    users.check_admin()

    if request.method == "GET":
        forum = forums.get_forum(forum_id)
        return render_template("forum_edit.html", forum=forum)

    users.check_csrf()

    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        if forums.update_forum(forum_id, name, description):
            return redirect("/forums")
        return render_template("error.html", message="Forum update failed")

    return render_template("error.html", message="Invalid request method")
