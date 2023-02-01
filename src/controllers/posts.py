from flask import session
from db import db

def get_posts_by_forum(forum_id):
    sql = """
        SELECT
            Posts.id,
            Posts.title,
            Posts.body,
            Posts.created_at,
            Posts.user_id,
            Users.username as author,
            count(Comments.post_id) as comment_count,
            count(distinct Likes_posts.user_id) as like_count, 
            count(distinct Likes_posts.user_id = :curr_user_id) as liked_by_curr_user
        FROM
            Posts
            LEFT JOIN Users ON Users.id = Posts.user_id
            LEFT JOIN Likes_posts ON Likes_posts.post_id = Posts.id
            LEFT JOIN Comments ON Comments.post_id = Posts.id
        WHERE
            forum_id = 1
        GROUP BY
            Posts.id,
            Users.username
        ORDER BY
            Posts.created_at DESC; 
    """
    result = db.session.execute(sql, {"forum_id":forum_id, "curr_user_id":session.get("user_id")})
    return result.fetchall()

def get_post(post_id):
    sql = """
        SELECT
            Posts.id,
            Posts.title,
            Posts.body,
            Posts.created_at,
            Posts.forum_id,
            Posts.user_id,
            Users.username as author,
            count(Comments.post_id) as comment_count,
            count(distinct Likes_posts.user_id) as like_count, 
            count(distinct Likes_posts.user_id = :curr_user_id) as liked_by_curr_user
        FROM
            Posts
            LEFT JOIN Users ON Users.id = Posts.user_id
            LEFT JOIN Likes_posts ON Likes_posts.post_id = Posts.id
            LEFT JOIN Comments ON Comments.post_id = Posts.id
        WHERE 
            Posts.id=:post_id
        GROUP BY
            Posts.id,
            Users.username
        ORDER BY 
            Posts.created_at DESC
    """
    result = db.session.execute(sql, {"post_id": post_id, "curr_user_id":session.get("user_id")})
    return result.fetchone()

def create_post(forum_id, title, body):
    try:
        sql = """
            INSERT INTO Posts (title, body, created_at, user_id, forum_id) 
            VALUES (:title, :body, NOW(), :user_id, :forum_id)
        """
        db.session.execute(
            sql, {"title":title, "body":body, "user_id":session["user_id"], "forum_id":forum_id}
        )
        db.session.commit()
        return True
    except:
        return False

def delete_post(post_id):
    try:
        sql = "DELETE FROM Posts WHERE id=:id"
        db.session.execute(sql, {"id":post_id})
        db.session.commit()
        return True
    except:
        return False
