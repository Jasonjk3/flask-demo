from werkzeug.exceptions import HTTPException

from application import app
from application.base import login_manager,log
from application.base.httpException import ServerError, APIException, NotLoggedInException


@app.errorhandler(Exception)
def framework_error(e):
    """
    AOP,全局异常处理
    :param e:
    :return:
    """
    log.error(e.description)
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    raise NotLoggedInException()