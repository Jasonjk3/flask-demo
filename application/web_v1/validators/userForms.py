from wtforms import StringField, FileField,BooleanField,IntegerField
from wtforms.validators import DataRequired

from application.base.baseForm import BaseForm as Form


class TokenForm(Form):
    token = StringField(validators=[DataRequired()])




class UserLoginForm(Form):
    account = StringField(validators=[DataRequired()])
    password = StringField(validators=[DataRequired()])
    remember_me = BooleanField(default=False)

class UserForm(Form):
    account = StringField(validators=[DataRequired()])
    password = StringField(validators=[DataRequired()])
    secret = StringField()
    headimg = FileField('头像')
    role = IntegerField(default=1)  # 用户身份
    nick_name = StringField()  # 昵称
    phone = StringField()  # 手机号


    # def validate_file(self, field):
    #     """
    #     验证文件的名字后缀是否合法
    #     :param field: file
    #     :return: None
    #     """
    #     if allowed_file(field.data.filename):
    #         return
    #     raise StopValidation('文件名后缀不合法！')