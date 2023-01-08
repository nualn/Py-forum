from app import app
from flask import render_template, request, redirect, url_for
from controllers import users, posts, comments, likes

@app.route("/forums/<int:forum_id>/posts/<int:post_id>/comments", methods=["GET", "POST"])
def comments_handler(forum_id, post_id):
    if request.method == "GET":
        comments_list = comments.get_comments_by_post(post_id)
        post = posts.get_post(post_id)
        return render_template("comments.html", post=post, comments=comments_list)

    if request.method == "POST":
        users.check_logged_in()
        users.check_csrf()
        body = request.form["body"]
        if comments.create_comment(post_id, body):
            return redirect(url_for("comments_handler", forum_id=forum_id, post_id=post_id))
        else:
            return render_template("error.html", message="Comment creation failed")

@app.route(
    "/forums/<int:forum_id>/posts/<int:post_id>/comments/<int:comment_id>/delete",
    methods=["POST"]
)
def comment_handler(forum_id, post_id, comment_id):
    comment = comments.get_comment(comment_id)
    users.check_owner(comment["user_id"])
    users.check_csrf()

    if comments.delete_comment(comment_id):
        return redirect(url_for("comments_handler", forum_id=forum_id, post_id=post_id))
    else:
        return render_template("error.html", message="Comment deletion failed")

@app.route("/forums/<int:forum_id>/posts/<int:post_id>/comments/like", methods=["POST"])
def comments_post_like_handler(forum_id, post_id):
    users.check_logged_in()
    users.check_csrf()
    if likes.like_post(post_id):
        return redirect(url_for("comments_handler", forum_id=forum_id, post_id=post_id))
    else:
        return render_template("error.html", message="Post like failed")

@app.route("/forums/<int:forum_id>/posts/<int:post_id>/comments/unlike", methods=["POST"])
def comments_post_unlike_handler(forum_id, post_id):
    users.check_logged_in()
    users.check_csrf()
    if likes.unlike_post(post_id):
        return redirect(url_for("comments_handler", forum_id=forum_id, post_id=post_id))
    return render_template("error.html", message="Post unlike failed")

@app.route(
    "/forums/<int:forum_id>/posts/<int:post_id>/comments/<int:comment_id>/like",
    methods=["POST"]
)
def comment_like_handler(forum_id, post_id, comment_id):
    users.check_logged_in()
    users.check_csrf()
    if likes.like_comment(comment_id):
        return redirect(url_for("comments_handler", forum_id=forum_id, post_id=post_id))
    return render_template("error.html", message="Comment like failed")

@app.route(
    "/forums/<int:forum_id>/posts/<int:post_id>/comments/<int:comment_id>/unlike",
    methods=["POST"]
)
def comment_unlike_handler(forum_id, post_id, comment_id):
    users.check_logged_in()
    users.check_csrf()
    if likes.unlike_comment(comment_id):
        return redirect(url_for("comments_handler", forum_id=forum_id, post_id=post_id))
    return render_template("error.html", message="Comment unlike failed")
