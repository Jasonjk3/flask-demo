from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

from application.base.baseForm import BaseForm as Form



class NewsForm(Form):
    title = StringField(validators=[DataRequired()])
    author = StringField(validators=[DataRequired()])
    date = StringField(validators=[DataRequired()])
    content = StringField(validators=[DataRequired()])


class GetNewsForm(Form):
    id = StringField()
    page = IntegerField(default=1)
    limit = IntegerField(default=10)


