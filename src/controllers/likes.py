from flask import session
from db import db

def like_post(post_id):
    try:
        sql = """
            INSERT INTO Likes_posts (user_id, post_id) 
            VALUES (:user_id, :post_id)
        """
        db.session.execute(sql, {"user_id":session["user_id"], "post_id":post_id})
        db.session.commit()
        return True
    except:
        return False

def unlike_post(post_id):
    try:
        sql = "DELETE FROM Likes_posts WHERE user_id=:user_id AND post_id=:post_id"
        db.session.execute(sql, {"user_id":session["user_id"], "post_id":post_id})
        db.session.commit()
        return True
    except:
        return False

def like_comment(comment_id):
    try:
        sql = """
            INSERT INTO Likes_comments (user_id, comment_id) 
            VALUES (:user_id, :comment_id)
        """
        db.session.execute(sql, {"user_id":session["user_id"], "comment_id":comment_id})
        db.session.commit()
        return True
    except:
        return False

def unlike_comment(comment_id):
    try:
        sql = "DELETE FROM Likes_comments WHERE user_id=:user_id AND comment_id=:comment_id"
        db.session.execute(sql, {"user_id":session["user_id"], "comment_id":comment_id})
        db.session.commit()
        return True
    except:
        return False
