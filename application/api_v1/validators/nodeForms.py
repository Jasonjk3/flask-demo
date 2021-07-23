from wtforms import StringField, IntegerField, FileField, BooleanField
from wtforms.validators import DataRequired

from application.base.baseForm import BaseForm as Form


class TokenForm(Form):
    token = StringField(validators=[DataRequired()])

class GetTokenForm(Form):
    secret = StringField(validators=[DataRequired()])

class AddNodeForm(Form):
    node_name = StringField(validators=[DataRequired()])
    ip = StringField(validators=[DataRequired()])
    port = StringField(validators=[DataRequired()])
    note = StringField()

class EditNodeForm(Form):
    node_id = IntegerField(validators=[DataRequired()])
    node_name = StringField()
    ip = StringField()
    port = StringField()
    note = StringField()


class NodeForm(Form):
    node_id = IntegerField(validators=[DataRequired()])
