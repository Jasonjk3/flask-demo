'''
@author: jasonfor
@contact: jasonforjob@qq.com
@file: node.py
@time: 2021/7/15 0015 23:22
@desc:
'''

from application.base import mysql_db as db

class Node(db.Model):
    """
    mysql ORM
    """
    # 定义表名
    __tablename__ = 'Nodes'

    node_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    node_name = db.Column(db.String(255), unique=True)
    ip = db.Column(db.String(255))
    port = db.Column(db.String(255))
    note = db.Column(db.String(255))
    status = db.Column(db.String(255))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()