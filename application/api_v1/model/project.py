'''
@author: jasonfor
@contact: jasonforjob@qq.com
@file: node.py
@time: 2021/7/15 0015 23:22
@desc:
'''

from application.base import mysql_db as db


class Project(db.Model):
    """
    项目表
    """
    # 定义表名
    __tablename__ = 'Project'
    # id = db.Column(db.String(255), primary_key=True)
    project_id = db.Column(db.Integer, primary_key=True,autoincrement=True)  # 项目id
    # node_id = db.Column(db.String(255))
    # spider_id = db.Column(db.String(255))
    # task_id = db.Column(db.String(255))
    project_name = db.Column(db.String(255), unique=True)
    create_time = db.Column(db.String(255))
    edit_time = db.Column(db.String(255))
    note = db.Column(db.String(255))
    status = db.Column(db.String(255))


class Spider(db.Model):
    """
    爬虫表
    """
    # 定义表名
    __tablename__ = 'Spider'
    spider_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    # task_id = db.Column(db.String(255))
    # node_id = db.Column(db.String(255))
    file_path = db.Column(db.String(255))
    spider_name = db.Column(db.String(255), unique=True)
    spider_config = db.Column(db.String(255))

    create_time = db.Column(db.String(255))
    edit_time = db.Column(db.String(255))
    note = db.Column(db.String(255))
    status = db.Column(db.String(255))


class Task(db.Model):
    """
    任务表
    """
    # 定义表名
    __tablename__ = 'Task'
    task_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    # spider_id = db.Column(db.String(255))
    # node_id = db.Column(db.String(255))
    # project_id = db.Column(db.String(255))
    task_name = db.Column(db.String(255), unique=True)
    start_time = db.Column(db.String(255))  # 启动时间
    end_time = db.Column(db.String(255))
    period = db.Column(db.String(255))  # 周期 按分钟算
    spider_config = db.Column(db.String(255))

    create_time = db.Column(db.String(255))
    edit_time = db.Column(db.String(255))
    note = db.Column(db.String(255))
    status = db.Column(db.String(255))


class TaskNodeList(db.Model):
    """
    任务下的节点表
    """
    # 定义表名
    __tablename__ = 'TaskNodeList'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    task_id = db.Column(db.Integer)
    node_id = db.Column(db.Integer)

class ProjectSpiderList(db.Model):
    """
    项目下的爬虫表
    """
    # 定义表名
    __tablename__ = 'ProjectSpiderList'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    project_id = db.Column(db.Integer)
    spider_id = db.Column(db.Integer)

if __name__ == '__main__':
    db.drop_all()
    db.create_all()