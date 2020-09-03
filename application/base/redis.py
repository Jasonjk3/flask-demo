"""
配置redis
"""
import redis

from application.base import log


class MyRedis(object):
    def __init__(self, host, port, password=None,db=1):
        self.host = host
        self.port = port
        self.password = password
        self.r=redis.Redis(host=self.host, port=self.port, password=self.password, db=db)
    # def initRedis(self, db=1):
    #     """
    #     初始化 redos
    #     :param db: 存放db的位置
    #     :param config: app.config 配置
    #     :return:
    #     """
    # 
    #     return redis.Redis(host=self.host, port=self.port, password=self.password, db=db)

    def write(self, key, value, expire=None):
        """
        写入键值对
        """

        r = self.r
        r.set(key, value, ex=expire)

    
    def read(self, key):
        """
        读取键值对内容
        """
        r = self.r
        value = r.get(key)
        return value.decode('utf-8') if value else value

    
    def hset(self, name, key, value):
        """
        写入hash表
        """
        r = self.r
        r.hset(name, key, value)

    
    def hmset(self, key, *value):
        """
        读取指定hash表的所有给定字段的值
        """
        r = self.r
        value = r.hmset(key, *value)
        return value

    
    def hget(self, name, key):
        """
        读取指定hash表的键值
        """
        r = self.r
        value = r.hget(name, key)
        return value.decode('utf-8') if value else value

    
    def hgetall(self, name):
        """
        获取指定hash表所有的值
        """
        r = self.r
        return r.hgetall(name)

    
    def delete(self, *names):
        """
        删除一个或者多个
        """
        r = self.r
        r.delete(*names)

    
    def hdel(self, name, key):
        """
        删除指定hash表的键值
        """
        r = self.r
        r.hdel(name, key)

    
    def expire(self, name, expire=None):
        """
        设置过期时间
        """
        r = self.r
        r.expire(name, expire)

    def load_dictionary(self):
        """
        加载系统配置
        :return:
        """
        log.info("加载配置中...")
        # 加载全局数据字典
        log.info("加载配置成功")