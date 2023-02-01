from app import app
from flask import render_template, request, session, redirect, abort, url_for
from controllers import users, posts, forums

@app.route("/forums/<int:forum_id>/posts", methods=["GET", "POST"])
def show_posts(forum_id):
    if request.method == "GET":
        posts_list = posts.get_posts_by_forum(forum_id)
        forum = forums.get_forum(forum_id)
        return render_template("posts.html", forum=forum, posts=posts_list)

    if request.method == "POST":
        users.check_logged_in()
        users.check_csrf()
        title = request.form["title"]
        body = request.form["body"]
        if posts.create_post(forum_id, title, body):
            return redirect(url_for("show_posts", forum_id=forum_id))
        else:
            return render_template("error.html", message="Post creation failed")

@app.route("/forums/<int:forum_id>/posts/<int:post_id>", methods=["DELETE", "PUT"])
def post(forum_id, post_id):
    users.check_owner(post_id)
    users.check_csrf()

    if request.method == "DELETE":
        if posts.delete_post(post_id):
            return redirect(url_for("show_posts", forum_id=forum_id))
        else:
            return render_template("error.html", message="Post deletion failed")

    if request.method == "PUT":
        title = request.form["title"]
        content = request.form["content"]
        if posts.update_post(post_id, title, content):
            return redirect(url_for("show_posts", forum_id=forum_id))
        else:
            return render_template("error.html", message="Post update failed")