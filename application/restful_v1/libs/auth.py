"""
权限管理
"""


class Auth:
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))
        # 运算符重载

        self.allow_module = self.allow_module + \
                            other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))

        return self


def is_in_scope(auth, endpoint):
    # 反射
    # globals会把当前模块下所有的变量包括在这里面编写的各种各样的类都变成一个字典
    # v1.view_func   v1.module_name+view_func
    # v1.red_name+view_func
    auth = globals()[auth]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in auth.forbidden:
        return False
    if endpoint in auth.allow_api:
        return True
    if red_name in auth.allow_module:
        return True
    else:
        return False


class AdminScope(Auth):
    # allow_api = ['v1.user+super_get_user',
    #              'v1.user+super_delete_user']
    allow_module = ['restful_v1.user', 'restful_v1.news']

    def __init__(self):
        # 排除
        pass
        # self + UserScope()


class UserScope(Auth):
    allow_module = ['restful_v1.user','restful_v1.news']
    # forbidden = ['v1.user+super_get_user',
    #              'v1.user+super_delete_user']

    def __init__(self):
        self + AdminScope()
    # allow_api = ['v1.user+get_user', 'v1.user+delete_user']
