from flask import current_app

from application.base import log, ajaxResponse
from application.base.httpException import ServerError
from application.restful_v1.libs.token_auth import generate_auth_token
from application.restful_v1.model.user import User


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
