from db import db
from flask import session

def get_posts_by_forum(forum_id):
    sql = """
        SELECT  Posts.id, 
                Posts.title, 
                Posts.body, 
                Posts.created_at, 
                Posts.user_id,
                Users.username as author,
                count(Comments.post_id) as comment_count
        FROM Posts 
        	LEFT JOIN Comments ON Comments.post_id = Posts.id
            LEFT JOIN Users ON Users.id = Posts.user_id
        WHERE forum_id=:forum_id
        GROUP BY Posts.id, Users.username
        ORDER BY Posts.created_at DESC; 
    """
    result = db.session.execute(sql, {"forum_id":forum_id})
    return result.fetchall()

def get_post(post_id):
    sql = """
        SELECT  Posts.id, 
                Posts.title, 
                Posts.body, 
                Posts.created_at, 
                Posts.forum_id,
                Posts.user_id,
                Users.username as author,
                count(Comments.post_id) as comment_count
        FROM Posts 
        	LEFT JOIN Comments ON Comments.post_id = Posts.id
            LEFT JOIN Users ON Users.id = Posts.user_id
        WHERE Posts.id=:post_id
        GROUP BY Posts.id, Users.username
        ORDER BY Posts.created_at DESC; 
    """
    result = db.session.execute(sql, {"post_id": post_id})
    return result.fetchone()

def create_post(forum_id, title, body):
    try:
        sql = """
            INSERT INTO Posts (title, body, created_at, modified_at, user_id, forum_id) 
            VALUES (:title, :body, NOW(), NOW(), :user_id, :forum_id)
        """
        db.session.execute(sql, {"title":title, "body":body, "user_id":session["user_id"], "forum_id":forum_id})
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
    
def update_post(post_id, title, content):
    try:
        sql = """
            UPDATE Posts 
            SET title=:title, content=:content, modified_at=NOW() 
            WHERE id=:id
        """
        db.session.execute(sql, {"id":post_id, "title":title, "content":content})
        db.session.commit()
        return True
    except:
        return False