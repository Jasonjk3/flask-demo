"""
配置redis
"""
import redis


class MyRedis():
    def __init__(self, host, port, password=None):
        self.host = host
        self.port = port
        self.password = password

    def initRedis(self, db=1):
        """
        初始化 redos
        :param db: 存放db的位置
        :param config: app.config 配置
        :return:
        """

        myRedis = redis.Redis(host=self.host, port=self.port, password=self.password, db=db)
        return myRedis

    def get_key(self, key):
        pass

    def save_key(self, key, value):
        pass

    def delete_key(self, key):
        pass
