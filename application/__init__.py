# 初始化app对象
from flask import Flask

app = Flask(__name__)

from config import setting
app.config.from_object(setting)

# 导入模块，注册蓝图
from application.api_v1 import create_blueprint_restful_v1
app.register_blueprint(create_blueprint_restful_v1(), url_prefix='/api_v1')

# from application.web_v1 import create_blueprint_web_v1
# app.register_blueprint(create_blueprint_web_v1(), url_prefix='/web_v1')




