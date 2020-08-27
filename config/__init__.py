# 获取配置文件信息
import configparser
from os import path


def initConf(file):
    try:
        conf = configparser.ConfigParser()
        conf.read(file, encoding="utf-8")
        return conf
    except Exception as ex:
        raise ex


config = initConf('./config.ini')


class BaseConfig(object):
    """
    公共配置环境
    """
    DEBUG = True
    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"

    # ASE加密密钥
    ASE_KEY = "RazdFTKyrwipPZHM"

    # Token时效
    TOKEN_EXPIRATION = 3600

    #
    SECRET_KEY = "Razdsd4dfddrwipPZHM"

    # 调度器
    CONFIG_SCHEDULER = False

    # MongoDB
    MONGO_URI = 'mongodb://localhost:27017/data'
    # MONGO_USERNAME = 'bjhee'
    # MONGO_PASSWORD = '111111'

    # 上传文件
    # 配置文件保存的目录，本参数必须设置；
    UPLOADED_PHOTO_DEST = path.join(path.dirname(path.abspath(__file__)), "aitms\static")
    # 配置允许的扩展名，其他的都是不允许
    UPLOADED_PHOTO_ALLOW = ['jpg', 'png']

class ProductConfig(BaseConfig):
    """
    正式配置环境
    """
    DEBUG = False
    CONFIG_NAME = 'ProductConfig'


class DevConfig(BaseConfig):
    """
    开发配置环境
    """
    CONFIG_NAME = 'DevConfig'


class TestConfig(BaseConfig):
    """
    测试配置环境
    """
    CONFIG_NAME = 'TestConfig'


settings = {
    'DevConfig': DevConfig,
    'TestConfig': TestConfig,
    'ProductConfig': ProductConfig
}
# 开发环境
setting = settings[config.get("BASE", "Settings")]
