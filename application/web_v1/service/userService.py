from flask import current_app
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from application.base import log, ajaxResponse, login_manager
from application.base.httpException import ServerError
from application.restful_v1.libs.token_auth import generate_auth_token
# from application.utils.upload import save_photo_file
from application.web_v1.models.user import User


@login_manager.user_loader
def load_user(user_id):
    return User.objects.with_id(user_id)



def login(form):
    # try:
    log.info("userService - login - Parameter:{}".format(form))
    user = User.objects(account=form.account.data).first()
    if user is None:
        return ajaxResponse.fail(message='账号不存在，请重试')
    # 先加密再对比
    if check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember_me.data)
        return ajaxResponse.success(message="登录成功")
    else:
        return ajaxResponse.fail(message='密码错误，请重试')


def logout():
    """
    登出
    :param form:
    :return:
    """
    log.info("userService - logout - Parameter:{}".format(''))
    logout_user()
    return ajaxResponse.success(message='注销成功')



def register(form):
    try:
        log.info("userService - register - Parameter:{}".format(form))
        verify=User.objects(account=form.account.data).first()
        if verify:
            return ajaxResponse.fail(message='用户已存在')
        user = User()
        user.account = form.account.data
        user.password = generate_password_hash(form.password.data)
        user.nick_name = form.nick_name.data
        user.phone = form.phone.data
        user.secret=generate_password_hash(form.account.data+form.password.data)
        # user.headimg=save_photo_file(form.headimg.data)
        result = user.save()
        if result:
            return ajaxResponse.success(message="注册成功")
        else:
            return ajaxResponse.fail(message='注册成功失败，请重试')
    except Exception as e:
        log.error("userService - register - 错误 - {}".format(e))
        raise ServerError()


def getSecret():
    try:
        log.info("getToken - getSecret - Parameter:{}".format(current_user.id))
        id=current_user.id
        user=User.objects.with_id(id)
        if user:
            return ajaxResponse.success(data=user.secret)
        else:
            return ajaxResponse.fail()
    except Exception as e:
        log.error("loginService - getSecret - 错误 - {}".format(e))
        raise ServerError()
