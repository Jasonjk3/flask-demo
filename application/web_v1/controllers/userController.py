from flask_login import login_required

from application.base.redPrint import RedPrint
from application.web_v1.service import userService
from application.web_v1.validators.userForms import UserLoginForm, UserForm

api = RedPrint('user_red')


@api.route('/test', methods=['GET'])
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

@api.route('/getSecret', methods=['GET'])
@login_required
def get_secret():
    """
    用户注册
    :return:
    """
    result = userService.getSecret()
    return result