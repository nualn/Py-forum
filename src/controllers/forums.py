from db import db

def get_forums():
    sql = "SELECT id, name, description FROM Forums"
    result = db.session.execute(sql)
    return result.fetchall()

def get_forum(id):
    sql = "SELECT id, name, description FROM Forums WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def create_forum(name, description):
    try:
        sql = "INSERT INTO Forums (name, description) VALUES (:name, :description)"
        db.session.execute(sql, {"name":name, "description":description})
        db.session.commit()
        return True
    except:
        return False

def delete_forum(forum_id):
    try:
        sql = "DELETE FROM Forums WHERE id=:id"
        db.session.execute(sql, {"id":forum_id})
        db.session.commit()
        return True
    except:
        return False

def update_forum(forum_id, name, description):
    try:
        sql = "UPDATE Forums SET name=:name, description=:description WHERE id=:id"
        db.session.execute(sql, {"id":forum_id, "name":name, "description":description})
        db.session.commit()
        return True
    except:
        return False