'''
@author: jasonfor
@contact: jasonforjob@qq.com
@file: __init__.py.py
@time: 2020/8/9 0009 21:41
@desc:web设计
'''
from flask import Blueprint

from application.web_v1.controllers import userController


def create_blueprint_web_v1():
    bp_v1 = Blueprint('web_v1', __name__)
    userController.api.register(bp_v1,url_prefix='/user')
    return bp_v1
