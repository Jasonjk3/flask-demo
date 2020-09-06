from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer \
    as Serializer, BadSignature, SignatureExpired

from application.base.httpException import AuthFailed, Forbidden
from application.restful_v1.libs.auth import is_in_scope
from application.restful_v1.model.user import User

UserTokenInfo = namedtuple('UserTokenInfo', ['secret'])
auth = HTTPBasicAuth()


@auth.verify_password
def verify_token(token, password):
    # verify_password 默认参数必须是account,password  这里用account当做token,密码为空就行
    # 请求头得有 Authorization  = basic account:password      账号密码包括冒号要basic64加密
    user_info = parse_token(token)
    if not user_info:
        return False
    else:
        # 解析成功
        user = User.objects(secret=user_info.secret).first()
        if user:
            # 1.在flask中，有一个专门用来存储用户信息的g对象，g的全称的为global。
            # 2.g对象在一次请求中的所有的代码的地方，都是可以使用的。
            g.user = user
            return True
        else:
            return False


def parse_token(token):
    """
    解析token
    :param token:
    :return:
    """
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired',
                         error_code=1003)
    secret = data['secret']
    auth = data['auth']
    allow = is_in_scope(auth, request.endpoint)
    if not allow:
        raise Forbidden()
    return UserTokenInfo(secret)


def generate_auth_token(secret, auth, expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        'secret': secret,
        'auth': auth
    })
