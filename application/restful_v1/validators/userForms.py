from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

from application.base.baseForm import BaseForm as Form


class TokenForm(Form):
    token = StringField(validators=[DataRequired()])

class GetTokenForm(Form):
    secret = StringField(validators=[DataRequired()])

class LoginForm(Form):
    account = StringField(validators=[DataRequired()])
    password=StringField(validators=[DataRequired()])




