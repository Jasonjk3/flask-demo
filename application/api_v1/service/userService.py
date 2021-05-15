from application.base.httpException import ServerError
from application.api_v1.model.user import User


from flask import current_app
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from application.base import log, ajaxResponse, login_manager
# from application.utils.upload import save_photo_file
from application.base import mysql_db



@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()



def login(form):
    # try:
    user = User.query.filter_by(username=form.username.data).first()
    print(user)
    if user is None:
        return ajaxResponse.fail(message='账号不存在，请重试')
    # 先加密再对比
    if check_password_hash(user.password, form.password.data):
        remember = form.remember_me.data or False
        login_user(user, remember=remember)
        return ajaxResponse.success(message="登录成功")
    else:
        return ajaxResponse.fail(message='密码错误，请重试')


def logout():
    """
    登出
    :param form:
    :return:
    """
    log.info("Parameter:{}".format(''))
    logout_user()
    return ajaxResponse.success(message='注销成功')



def register(form):
    verify = User.query.filter_by(username=form.username.data).first()
    if verify:
        return ajaxResponse.fail(message='用户已存在')
    user = User()
    user.username = form.username.data
    user.password = generate_password_hash(form.password.data)
    try:
        mysql_db.session.add(user)
        mysql_db.session.commit()
    except:
        return ajaxResponse.fail(message='注册失败，请重试')
    return ajaxResponse.success(message="注册成功")




def getToken(form):
    try:
        log.info("成功 - Parameter:{}".format(form))
        user = User.objects(secret=form.secret.data).first()
        if user:
            expiration = current_app.config['TOKEN_EXPIRATION']
            role = {1: "UserScope", 2: "AdminScope"}
            token = generate_auth_token(secret=form.secret.data, auth=role[user.role], expiration=expiration)
            model = {'token': token.decode('ascii')}
            return ajaxResponse.success(data=model, message="返回token成功")
        else:
            return ajaxResponse.fail(message="secret无效")
    except Exception as e:
        log.error("错误 - {}".format(e))
        raise ServerError()
