'''
@author: jasonfor
@contact: jasonforjob@qq.com
@file: mongodb.py
@time: 2020/8/4 0004 22:53
@desc:
'''

from mongoengine import *
from flask_pymongo import PyMongo
import pymongo
def init_mongoengine_MongoDb(app):
    mongo = PyMongo(app)
    connect(host=app.config['MONGO_URI'], connect=False)  # 需要有默认连接

    return mongo

def initMongoDb(uri=None, dbname=''):
    mongo = pymongo.MongoClient(uri)  # 连接
    return mongo[dbname]
