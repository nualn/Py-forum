from app import app
from flask import render_template, request, redirect, url_for
from controllers import users, posts, forums, likes

@app.route("/forums/<int:forum_id>/posts", methods=["GET", "POST"])
def posts_handler(forum_id):
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
            return redirect(url_for("posts_handler", forum_id=forum_id))
        else:
            return render_template("error.html", message="Post creation failed")

@app.route("/forums/<int:forum_id>/posts/<int:post_id>/delete", methods=["POST"])
def post_handler(forum_id, post_id):
    post = posts.get_post(post_id)
    users.check_owner(post["user_id"])
    users.check_csrf()

    if posts.delete_post(post_id):
        return redirect(url_for("posts_handler", forum_id=forum_id))
    else:
        return render_template("error.html", message="Post deletion failed")

@app.route("/forums/<int:forum_id>/posts/<int:post_id>/like", methods=["POST"])
def post_like_handler(forum_id, post_id):
    users.check_logged_in()
    users.check_csrf()
    if likes.like_post(post_id):
        return redirect(url_for("posts_handler", forum_id=forum_id))
    else:
        return render_template("error.html", message="Post like failed")

@app.route("/forums/<int:forum_id>/posts/<int:post_id>/unlike", methods=["POST"])
def post_unlike_handler(forum_id, post_id):
    users.check_logged_in()
    users.check_csrf()
    if likes.unlike_post(post_id):
        return redirect(url_for("posts_handler", forum_id=forum_id))
    else:
        return render_template("error.html", message="Post unlike failed")