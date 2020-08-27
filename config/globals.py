from enum import Enum


class CodeEnum(Enum):
    """
    状态码
    """
    SUCCESS = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    ERROR = 500

    ERROR_AUTH_CHECK_TOKEN_FAIL = 10001
    ERROR_AUTH_CHECK_TOKEN_TIMEOUT = 10002
    ERROR_AUTH_TOKEN = 10003
    ERROR_AUTH = 10004

class MessageEnum(Enum):
    """
    消息
    """
    SUCCESS = "操作成功"
    ERROR = "操作失败"


class DictionaryEnum(Enum):
    """
    字典
    """
    pass

