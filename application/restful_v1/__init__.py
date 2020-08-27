'''
@author: jasonfor
@contact: jasonforjob@qq.com
@file: __init__.py.py
@time: 2020/8/9 0009 21:41
@desc:restful风格API
'''
from flask import Blueprint


def create_blueprint_restful_v1():
    """
    注册红图
    :return:
    """
    from application.restful_v1.controller import userController
    from application.restful_v1.controller import newsController
    bp_v1 = Blueprint('restful_v1', __name__)
    userController.api.register(bp_v1, url_prefix='/user')
    newsController.api.register(bp_v1, url_prefix='/news')
    return bp_v1
