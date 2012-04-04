#-*- coding:utf-8 -*-

from functools import wraps
from flask import g, redirect

def require_login(redir=None):
    def _(f):
        @wraps(f)
        def __(*a, **kw):
            if not g.user:
                return redir or redirect("/home")
            return f(*a, **kw)
        return __
    return _
