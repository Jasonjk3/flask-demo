from wtforms import StringField, IntegerField, FileField, BooleanField
from wtforms.validators import DataRequired

from application.base.baseForm import BaseForm as Form


class TokenForm(Form):
    token = StringField(validators=[DataRequired()])

class GetTokenForm(Form):
    secret = StringField(validators=[DataRequired()])

class UserLoginForm(Form):
    username = StringField(validators=[DataRequired()])
    password = StringField(validators=[DataRequired()])
    remember_me = BooleanField(default=False)

class UserForm(Form):
    username = StringField(validators=[DataRequired()])
    password = StringField(validators=[DataRequired()])
    # secret = StringField()
    # headimg = FileField('头像')
    # role = IntegerField(default=1)  # 用户身份
    # nick_name = StringField()  # 昵称
    # phone = StringField()  # 手机号





