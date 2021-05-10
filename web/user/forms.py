from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, SelectField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo,ValidationError
from web.models import User

class UserSearchForm(FlaskForm):
    user_type = [(0, 'All'),
               (1, 'Managment'),
               (2, 'User')]
    usertype_select = SelectField('select user type:', choices=user_type,coerce=int)
    search = SubmitField('search')

