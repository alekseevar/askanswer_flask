import sqlite3
from flask import g


def connect_db():
    sql = sqlite3.connect('/Users/ruslanaalekseeva/ruslana/flask_udemy/project3/questions.db')
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
