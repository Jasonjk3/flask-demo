'''
@author: jasonfor
@contact: jasonforjob@qq.com
@file: ProjectController.py
@time: 2021/7/14 0014 22:30
@desc:
'''
from application.api_v1.service import projectService
from application.base.redPrint import RedPrint

api = RedPrint('project')


@api.route('/test', methods=['GET'])
def test():
    return 'test'


@api.route('/getProjectsList', methods=['GET'])
def getProjectsListController():
    """
    获取项目列表
    :return:
    """
    form = ''
    result = projectService.getProjectsList(form)
    return result


@api.route('/getProject', methods=['GET'])
def getProjectController():
    """
    获取一个项目
    :return:
    """
    form = ''
    result = projectService.getProject(form)
    return result


@api.route('/addProject', methods=['GET'])
def addProjectController():
    """
    新增一个项目
    :return:
    """
    form = ''
    result = projectService.addProject(form)
    return result


@api.route('/deleteProject', methods=['GET'])
def deleteProjectController():
    """
    删除一个项目
    :return:
    """
    form = ''
    result = projectService.deleteProject(form)
    return result


@api.route('/editProject', methods=['GET'])
def editProjectController():
    """
    修改一个项目
    :return:
    """
    form = ''
    result = projectService.editProject(form)
    return result

