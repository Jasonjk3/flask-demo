'''
@author: jasonfor
@contact: jasonforjob@qq.com
@file: user.py
@time: 2020/8/16 0016 16:32
@desc:
'''
from flask_login import UserMixin
from mongoengine import *


class User(UserMixin,Document):
    # uid = SequenceField(primary_key=True)  # 自增id
    # create_time = StringField(max_length=100)  # 账号创建时间
    account = StringField(max_length=50)
    password = StringField(max_length=200)
    secret=StringField(max_length=200)
    headimg = StringField(max_length=200)  # 头像
    role = StringField(max_length=100)  # 用户身份
    nick_name = StringField(max_length=100)  # 昵称
    phone = StringField(max_length=100)  # 手机号
    meta = {"collection": "users"}



