from flask_login import login_required

from application.base import login_manager
from application.base.redPrint import RedPrint
from application.api_v1.service import userService
from application.api_v1.validators.userForms import GetTokenForm, UserForm, UserLoginForm

api=RedPrint('user')


# 自定义未登录处理函数
# 如果你不想使用默认的规则，那么你也可以自定义未登录情况的处理函数，只需要使用 login_manager 的 unauthorized_handler 装饰器即可。
@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return 'bad'

@api.route('/test',methods=['GET'])
@login_required
def test():
    return 'test'

@api.route('/login', methods=['POST'])
def login():
    """
    用户登录
    :return:
    """
    form = UserLoginForm()
    if form.validate_for_api():
        result = userService.login(form)
        return result

@api.route('/logout', methods=['GET'])
@login_required
def logout():
    """
    用户注销
    :return:
    """
    result = userService.logout()
    return result


@api.route('/register', methods=['POST'])
def register():
    """
    用户注册
    :return:
    """
    form = UserForm()
    if form.validate_for_api():
        result = userService.register(form)
        return result


@api.route('/getToken', methods=['GET'])
def get_Token():
    """
    获取Toekn
    :return:
    """
    form = GetTokenForm()
    if form.validate_for_api():
        result=userService.getToken(form)
        return result




