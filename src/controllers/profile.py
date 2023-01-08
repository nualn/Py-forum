from db import db
from flask import session

def get_user_info(user_id):
    sql = """
        SELECT
            Users.id,
            Users.username
        FROM
            Users
        WHERE
            Users.id = :user_id
    """
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchone()

def get_posts_by_user(user_id):
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
            count(
                distinct Likes_posts.user_id = :curr_user_id
            ) as liked_by_curr_user
        FROM
            Posts
            LEFT JOIN Users ON Users.id = Posts.user_id
            LEFT JOIN Likes_posts ON Likes_posts.post_id = Posts.id
            LEFT JOIN Comments ON Comments.post_id = Posts.id
        WHERE 
            Posts.user_id=:user_id
        GROUP BY
            Posts.id,
            Users.username
        ORDER BY
            Posts.created_at DESC
    """
    result = db.session.execute(sql, {"user_id":user_id, "curr_user_id":session.get("user_id")})
    return result.fetchall()

def get_comments_by_user(user_id):
    sql = """
        SELECT
            Comments.id,
            Comments.body,
            Comments.created_at,
            Comments.post_id,
            Comments.user_id,
            Users.username as author,
            Posts.title as post_title,
            Posts.forum_id,
            count(distinct Likes_comments.user_id) as like_count, 
            count(
                distinct Likes_comments.user_id = :curr_user_id
            ) as liked_by_curr_user
        FROM
            Comments
            LEFT JOIN Users ON Users.id = Comments.user_id
            LEFT JOIN Likes_comments ON Likes_comments.comment_id = Comments.id
            LEFT JOIN Posts ON Posts.id = Comments.post_id
        WHERE 
            Comments.user_id=:user_id
        GROUP BY
            Comments.id,
            Users.username,
            Posts.title,
            Posts.forum_id
        ORDER BY
            Comments.created_at DESC
    """
    result = db.session.execute(sql, {"user_id":user_id, "curr_user_id":session.get("user_id")})
    return result.fetchall()