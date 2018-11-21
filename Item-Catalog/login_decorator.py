from functools import wraps
from flask import redirect,flash
from flask import session as login_session

def login_required(f):
    @wraps(f)
    def x(*args, **kwargs):
        if 'username' not in login_session:
            flash("You are not allowed to access there")
            return redirect('/login')
        return f(*args, **kwargs)
    return x