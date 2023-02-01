from flask import render_template, request, redirect

from app import app
from controllers import profile, users

@app.route("/users/<int:user_id>/profile", methods=["GET"])
def profile_handler(user_id):
    user = profile.get_user_info(user_id)
    posts = profile.get_posts_by_user(user_id)
    comments = profile.get_comments_by_user(user_id)
    return render_template("profile.html", user=user, posts=posts, comments=comments)

@app.route("/users/<int:user_id>/toggle_admin", methods=["POST"])
def toggle_admin_handler(user_id):
    users.check_csrf()
    users.check_admin()

    users.toggle_admin(user_id)
    return redirect(request.referrer)
