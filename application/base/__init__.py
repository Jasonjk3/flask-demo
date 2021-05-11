from application import app
# 存放需初始化的对象

# 实例化日志模块

from application.base.log import initLog

log = initLog(app.config['LOG_LEVEL'])
log.info("初始化对象中...")
log.info(f"日志等级:{app.config['LOG_LEVEL']}")

# 实例化数据库
from application.base.mongodb import initMongoDb

# mongo = init_mongoengine_MongoDb(app)
mongo_data = initMongoDb(app.config['MONGO_URI'],app.config['MONGO_DATASERVER'])
log.info("数据库连接对象:"+app.config['MONGO_URI'])

from flask_sqlalchemy import SQLAlchemy
mysql_db = SQLAlchemy(app)

# 实例化edis
from application.base.redis import MyRedis

redis = MyRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
redis_conf = MyRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'],db=2)
redis_user = MyRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'],db=3)

redis_conf.load_dictionary()


# 实例化flask_login
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = "strong"  # 会话保护
login_manager.init_app(app)

# CSRF 保护
from flask_wtf.csrf import CSRFProtect
CSRFProtect(app)

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

log.info("初始化对象成功")
