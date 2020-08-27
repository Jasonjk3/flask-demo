'''
@author: jasonfor
@contact: jasonforjob@qq.com
@file: news.py
@time: 2020/8/23 0023 23:36
@desc:
'''
from mongoengine import *

class News(Document):
    title = StringField(max_length=50)
    author = StringField(max_length=50)
    date = DateTimeField()
    content = StringField()