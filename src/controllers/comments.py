from flask import session
from db import db

def get_comments_by_post(post_id):
    sql = """
        SELECT
            Comments.id,
            Comments.body,
            Comments.created_at,
            Comments.user_id,
            Users.username as author,
            count(distinct Likes_comments.user_id) as like_count,
            count(
                distinct Likes_comments.user_id = :curr_user_id
            ) as liked_by_curr_user
        FROM
            Comments
            LEFT JOIN Users ON Users.id = Comments.user_id
            LEFT JOIN Likes_comments ON Likes_comments.comment_id = Comments.id
        WHERE
            post_id = :post_id
        GROUP BY Comments.id, Users.username
        ORDER BY
            created_at ASC; 
    """
    result = db.session.execute(sql, {"post_id":post_id, "curr_user_id":session.get("user_id")})
    return result.fetchall()

def get_comment(comment_id):
    sql = "SELECT * FROM Comments WHERE id=:comment_id;"
    result = db.session.execute(sql, {"comment_id":comment_id})
    return result.fetchone()

def create_comment(post_id, body):
    try:
        sql = """
            INSERT INTO Comments (body, created_at, user_id, post_id) 
            VALUES (:body, NOW(), :user_id, :post_id)
        """
        db.session.execute(sql, {"body":body, "user_id":session["user_id"], "post_id":post_id})
        db.session.commit()
        return True
    except:
        return False

def delete_comment(comment_id):
    try:
        sql = "DELETE FROM Comments WHERE id=:id"
        db.session.execute(sql, {"id":comment_id})
        db.session.commit()
        return True
    except:
        return False
