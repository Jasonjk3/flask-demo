from application.base.redPrint import RedPrint
from application.restful_v1.libs.token_auth import auth
from application.restful_v1.service import userService
from application.restful_v1.validators.userForms import GetTokenForm

api=RedPrint('user_red')

@api.route('/test',methods=['GET'])
@auth.login_required
def test():
    return 'test'



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




