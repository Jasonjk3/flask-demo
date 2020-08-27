from flask import request
from wtforms import Form

from application.base import log
from application.base.httpException import ParameterException
"""
wtforms 继承基类
"""

class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()

        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self,):
        valid = super(BaseForm, self).validate()
        # 如果校验失败，返回自定义函数
        if not valid:
            # form errors
            log.error(self.errors)
            raise ParameterException(msg=self.errors)
        return self
