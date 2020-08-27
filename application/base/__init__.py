from application import app
# 存放需初始化的对象

# 实例化日志模块

from application.base.log import initLog

log = initLog()

# 实例化数据库
from application.base.mongodb import initMongoDb

mongo = initMongoDb(app)

# 实例化edis
from application.base.redis import MyRedis

redis = MyRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
myRedis = redis.initRedis(db=1)
myRedis_conf = redis.initRedis(db=2)
myRedis_user = redis.initRedis(db=3)

# 实例化flask_login
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = "strong"  # 会话保护
login_manager.init_app(app)

# CSRF 保护
# from flask_wtf.csrf import CsrfProtect
# CsrfProtect(app)

# 初始化upload
# from flask_uploads import configure_uploads,UploadSet
# files = UploadSet('files')
# photos = UploadSet(name='photos')
# configure_uploads(app, [files, photos])

# 配置定时器任务
if app.config['CONFIG_SCHEDULER']:
    from application.base.scheduler import initScheduler

    initScheduler(app, log)

# 配置全局跨域
from flask_cors import CORS

CORS(app, supports_credentials=True)
