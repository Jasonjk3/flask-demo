from application.base import log, ajaxResponse
from application.base.httpException import ServerError



def getProjectsList(form):
    try:
        return ajaxResponse.success(message="保存成功")
    except Exception as e:
        log.error("错误 - {}".format(e))
        raise ServerError()


def getProject(form):
    try:
        return ajaxResponse.success(message="保存成功")
    except Exception as e:
        log.error("错误 - {}".format(e))
        raise ServerError()


def addProject(form):
    try:
        return ajaxResponse.success(message="保存成功")
    except Exception as e:
        log.error("错误 - {}".format(e))
        raise ServerError()


def deleteProject(form):
    try:
        return ajaxResponse.success(message="保存成功")
    except Exception as e:
        log.error("错误 - {}".format(e))
        raise ServerError()


def editProject(form):
    try:
        return ajaxResponse.success(message="保存成功")
    except Exception as e:
        log.error("错误 - {}".format(e))
        raise ServerError()

