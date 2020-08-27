from flask import jsonify

from config.globals import CodeEnum


# ajax 返回json格式

def success(is_success=True, code=CodeEnum.SUCCESS.value, data=None, message='执行成功'):
    result_json = {
        'isSuccess': is_success,
        'code': code,
        'data': data,
        'message': message
    }

    return jsonify(result_json)


def fail(is_success=False, code=CodeEnum.ERROR.value, data=None, message='执行失败'):
    result_json = {
        'isSuccess': is_success,
        'code': code,
        'data': data,
        'message': message
    }
    return jsonify(result_json)
