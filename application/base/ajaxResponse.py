from flask import jsonify

from config.globals import CodeEnum


# ajax 返回json格式

def success(message='执行成功', data=None,code=CodeEnum.SUCCESS.value):
    result_json = {
        'code': code,
        'data': data,
        'message': message
    }

    return jsonify(result_json)


def fail(message='执行失败', data=None ,code=CodeEnum.ERROR.value):
    result_json = {
        'code': code,
        'data': data,
        'message': message
    }
    return jsonify(result_json)
