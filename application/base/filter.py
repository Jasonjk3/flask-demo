import re

from flask import request
from application import app
from application.base import ajaxResponse


# 拦截器,每次的请求进来都会做的操作
@app.before_request
def before_action():
     # 获取当前请求的路由（路径）
    a = request.path
    u = a.split('/')
    if len(a) > 2:
      if u[1] == 'index':
        print('success')
    else:
        return "无权限请求"

@app.before_request
def XSSProtection():
    dr = re.compile(r'<[^>]+>', re.S)
    for (k, v) in request.args.items():
        if(re.search(dr, v) is not None):
            return ajaxResponse.fail(message="请不要使用html标签")
