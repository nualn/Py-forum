from db import db
from flask import session

def get_comments_by_post(post_id):
    sql = """
        SELECT  id, 
                body, 
                created_at, 
                modified_at, 
                user_id 
        FROM Comments 
        WHERE post_id=:post_id
        ORDER BY created_at ASC;
    """
    result = db.session.execute(sql, {"post_id":post_id})
    return result.fetchall()

def get_comment(comment_id):
    sql = "SELECT * FROM Comments WHERE id=:comment_id;"
    result = db.session.execute(sql, {"comment_id":comment_id})
    return result.fetchone()

def create_comment(post_id, body):
    try:
        sql = """
            INSERT INTO Comments (body, created_at, modified_at, user_id, post_id) 
            VALUES (:body, NOW(), NOW(), :user_id, :post_id)
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

def update_comment(comment_id, body):
    try:
        sql = """
            UPDATE Comments 
            SET body=:body, modified_at=NOW() 
            WHERE id=:id
        """
        db.session.execute(sql, {"id": comment_id, "body":body})
        db.session.commit()
        return True
    except:
        return False