from application.api_v1.model.node import Node
from application.api_v1.validators.nodeForms import AddNodeForm
from application.base import log, ajaxResponse
from application.base.httpException import ServerError
from application.base import mysql_db as db


def getNodesList():
    try:
        models = Node.query.all()
        datas=[]
        for model in models:
            data = {
                'node_id': model.node_id,
                'node_name': model.node_name,
                'ip': model.ip,
                'port': model.port,
                'note': model.note,
                'status': model.status
            }
            datas.append(data)
        return ajaxResponse.success(message="保存成功",data=datas)
    except Exception as e:
        log.error("错误 - {}".format(e))
        raise ServerError()


def getNode(form):
    try:
        model = Node.query.filter_by(node_id=form.node_id.data).first()
        if model is None:
            return ajaxResponse.fail('node不存在')
        data = {
            'node_id':model.node_id,
            'node_name':model.node_name,
            'ip':model.ip,
            'port': model.port,
            'note':model.note,
            'status':model.status
        }
        return ajaxResponse.success(message="保存成功",data=data)
    except Exception as e:
        log.error("错误 - {}".format(e))
        raise ServerError()


def addNode(form: AddNodeForm):
    try:
        hasName = Node.query.filter_by(node_name=form.node_name.data).first()
        if hasName:
            return ajaxResponse.fail(message='node_name 已存在，请更换')
        hasName = Node.query.filter_by(ip=form.ip.data,port=form.port.data).first()
        if hasName:
            return ajaxResponse.fail(message='ip:port 已存在，请更换')
        model = Node()
        model.node_name = form.node_name.data
        model.ip = form.ip.data
        model.port = form.port.data
        model.note = form.note.data

        db.session.add(model)
        db.session.commit()

        return ajaxResponse.success(message="新增成功")
    except Exception as e:
        log.error("错误 - {}".format(e))
        db.session.rollback()
        raise ServerError()


def deleteNode(form):
    try:
        model = Node.query.filter_by(node_id=form.node_id.data).first()
        if model is None:
            return ajaxResponse.fail(message='node_id 不存在，请更换')
        db.session.delete(model)
        db.session.commit()
        return ajaxResponse.success(message="删除成功")
    except Exception as e:
        log.error("错误 - {}".format(e))
        db.session.rollback()
        raise ServerError()


def editNode(form):
    try:
        model = Node.query.filter_by(node_id=form.node_id.data).first()
        if model is None:
            return ajaxResponse.fail(message='node不存在')

        model.node_name = form.node_name.data
        model.ip = form.ip.data
        model.port = form.port.data
        model.note = form.note.data
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            return ajaxResponse.fail('更新失败,可能部分字段已存在')
        return ajaxResponse.success(message="保存成功")
    except Exception as e:
        log.error("错误 - {}".format(e))
        raise ServerError()
