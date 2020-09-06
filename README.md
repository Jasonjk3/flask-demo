# flask-demo
**flask框架通用后台架构**

该项目主要由flask+redis+mongodb构成
集成了flask众多组件:
Flask-APScheduler
Flask-Cors
Flask-HTTPAuth
Flask-Login
flask-mongoengine
Flask-PyMongo
Flask-Script
Flask-SQLAlchemy
Flask-Uploads
Flask-WTF

### 两种设计风格可供选择:
WEB 通用 经典MVC设计模式
RESTful API设计风格
后续将不断完善该项目

![架构图](https://github.com/Jasonjk3/temp/blob/master/images/%E6%9E%B6%E6%9E%84.png "架构图")


## 特点
### 1.红图
在模块化管理中采用更划分细腻的自定义蓝图————红图，蓝图用拆分较大的模块，红图拆分模块下的具体的业务对象。
![红图](https://github.com/Jasonjk3/temp/blob/master/images/red_print.jpg "红图")

### 2.用户令牌
用token校验身份，是前后端交互的常用方式。
它有以下特性：
- 会失效
- 加密
- 可以根据它拿到用户的信息

### 3.权限管理


### 4.自定义异常处理



##主要功能
### 1.定时器


### 2.日志

### 3.文件上传

### 4.表单验证

### 5.redis调用封装

### 6.mongoengine

### 4.flask-login

# 持续更新中...
