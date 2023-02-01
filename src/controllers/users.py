import secrets
from db import db
from flask import session, request, abort
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT id, username, password, is_admin FROM Users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            session["is_admin"] = user.is_admin
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO Users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def logout():
    del session["user_id"] 
    del session["username"]
    del session["is_admin"]
    del session["csrf_token"]

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

def check_admin():
    if not session["is_admin"]:
        abort(403)

def check_logged_in():
    if not session.get("user_id"):
        abort(403)

def check_owner(content_id):
    if content_id != session["user_id"]:
        abort(403)