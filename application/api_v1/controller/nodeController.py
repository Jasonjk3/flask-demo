'''
@author: jasonfor
@contact: jasonforjob@qq.com
@file: nodeController.py
@time: 2021/7/14 0014 22:30
@desc:
'''
from application.api_v1.service import nodeService
from application.api_v1.validators.nodeForms import AddNodeForm, NodeForm, EditNodeForm
from application.base.redPrint import RedPrint

api = RedPrint('node')


@api.route('/test', methods=['GET'])
def test():
    return 'test'


@api.route('/getNodesList', methods=['GET'])
def getNodesListController():
    """
    获取scrapyd  节点列表
    :return:
    """
    result = nodeService.getNodesList()
    return result


@api.route('/getNode', methods=['GET'])
def getNodeController():
    """
    获取一个scrapyd 节点
    :return:
    """
    form = NodeForm()
    if form.validate_for_api():
        result = nodeService.getNode(form)
        return result


@api.route('/addNode', methods=['POST'])
def addNodeController():
    """
    新增一个scrapyd 节点
    :return:
    """
    form = AddNodeForm()
    if form.validate_for_api():
        result = nodeService.addNode(form)
        return result


@api.route('/deleteNode', methods=['GET'])
def deleteNodeController():
    """
    删除一个scrapyd 节点
    :return:
    """
    form = NodeForm()
    if form.validate_for_api():
        result = nodeService.deleteNode(form)
        return result


@api.route('/editNode', methods=['POST'])
def editNodeController():
    """
    修改一个scrapyd 节点
    :return:
    """
    form = EditNodeForm()
    if form.validate_for_api():
        result = nodeService.editNode(form)
        return result
