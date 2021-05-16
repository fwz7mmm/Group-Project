from flask import render_template, url_for,Blueprint,redirect,flash,request
from flask_login import login_user, logout_user, login_required,current_user
from web import get_logger,bcrypt,db
from flask_login import login_required
from flask_mail import Message
from web import mail
from web.models import User
from web.auth.forms import ForgetPasswordForm
import random
import string
logger = get_logger(__name__)

auth = Blueprint('auth', __name__)


def get_random_string():
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return  result_str

def send_mail(email):
    random_password = get_random_string()

    msg = Message('Hello from the  WebQuiz!', sender='wenwuw121wwwww@gmail.com', recipients=[str(email)],
                  body="Hey this is new password")
    msg.html = "<b> New password is " + random_password + "</b>"
    mail.send(message=msg)

    return random_password


@auth.route("/register",methods=['POST','Get'])

def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if  request.method == 'POST':
        logger.debug(request.form)
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')
        birthday = request.form.get('birthday')

        is_username = User.query.filter_by(username=username).first()
        is_email = User.query.filter_by(email=email).first()
        is_phone = User.query.filter_by(phone=phone).first()
        if is_username:
            flash('username exists')
        if is_email:
            flash('email exists')
        if is_phone:
            flash('phone exists')
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(
            username = username,
            email=email,
            password=hashed_password,
            phone = phone,
            birth = birthday,
            status = True,
            user_type = 1,
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    logger.debug('login')
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if  request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        logger.debug(request.form)
        user = User.query.filter_by(username=username).first()
        if user and user.status == 0 :
            flash('user not able use')
        elif user and bcrypt.check_password_hash(user.password.encode('utf-8'), password.encode('utf-8')):
            login_user(user, True)
            return redirect(url_for('main.content'))
        else:
            flash('username or password error')
    return render_template('auth/login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have login out')
    return redirect(url_for('auth.login'))


@auth.route("/forget_password",methods=['POST','GET'])
def forget_password():
    form = ForgetPasswordForm()
    if  request.method == 'POST' :
        email=request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user :
            newpassword=send_mail(user.email)
            logger.debug(newpassword)
            user.password = bcrypt.generate_password_hash(newpassword).decode('utf-8')
            logger.debug(user.password)
            db.session.commit()
            flash('One message have send to you email with new password','success')
            return redirect(url_for('auth.login'))
        else:
            flash('email is wrong')

    return render_template('auth/forgetpassword.html',form=form)

