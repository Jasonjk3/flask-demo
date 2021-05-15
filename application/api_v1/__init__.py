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
    from application.api_v1.controller import newsController,weiboController,userController
    bp_v1 = Blueprint('api_v1', __name__)
    userController.api.register(bp_v1, url_prefix='/user')
    newsController.api.register(bp_v1, url_prefix='/news')
    weiboController.api.register(bp_v1, url_prefix='/weibo')
    return bp_v1
