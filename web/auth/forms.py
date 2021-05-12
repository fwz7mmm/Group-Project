from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, SelectField, TextAreaField, HiddenField,IntegerField,DateField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo,ValidationError
from web.models import User

class RegisterForm(FlaskForm):
    username = StringField('User Name:', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = IntegerField('Phone:')
    birth = DateField('Birth:')
    password = PasswordField('PassWord', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Name exists')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email exists')

    def validate_phone(self, phone):
        user = User.query.filter_by(phone=phone.data).first()
        if user:
            raise ValidationError('Phone exists')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 64), ])
    password = PasswordField('password', validators=[DataRequired()])
    rememberme = BooleanField('remember me')
    submit = SubmitField('submit')

class ForgetPasswordForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('submit')