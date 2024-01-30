from wtforms import Form
from wtforms import SearchField, TextAreaField, RadioField, StringField, SelectField,DecimalField

class UserForm(Form):
    x1=DecimalField("x1")
    y1=DecimalField("y1")
    x2=DecimalField("x2")
    y2=DecimalField("y2")