# 获取配置文件信息
from os import path


class BaseConfig(object):
    """
    公共配置环境
    """
    DEBUG = True

    # 程序运行IP端口
    RUN_IP = "0.0.0.0"
    RUN_PORT = "5003"

    # in [ERROR DEBUG WARNING INFO]
    LOG_LEVEL = 'ERROR'

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
    MONGO_URI = 'mongodb://localhost:27017'
    MONGO_DATASERVER = 'Data_Server'

    # mysql 数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:zh1132@139.159.204.92:3306/spider'
    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True
    # 禁止自动提交数据处理
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False

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
setting = settings['ProductConfig']
