from app import app
from flask import render_template
from controllers import profile

@app.route("/users/<int:user_id>/profile", methods=["GET"])
def profile_handler(user_id):
    user = profile.get_user_info(user_id)
    posts = profile.get_posts_by_user(user_id)
    comments = profile.get_comments_by_user(user_id)
    return render_template("profile.html", user=user, posts=posts, comments=comments)