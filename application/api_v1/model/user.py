'''
@author: jasonfor
@contact: jasonforjob@qq.com
@file: user.py
@time: 2020/8/16 0016 16:32
@desc:
'''
from flask_login._compat import unicode

from application.base import mysql_db as db

class User(db.Model):
    """
    mysql ORM
    """
    # 定义表名
    __tablename__ = 'user'
    username = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.username)

