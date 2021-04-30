from flask import render_template, url_for,Blueprint,redirect,flash,request
from flask_login import login_user, logout_user, login_required,current_user
from web import get_logger,bcrypt,db
from flask_login import login_required
from web.auth.forms import RegisterForm
from web.models import User
logger = get_logger(__name__)
auth = Blueprint('auth', __name__)


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

        username = User.query.filter_by(username=username).first()
        email = User.query.filter_by(email=email).first()
        phone = User.query.filter_by(phone=phone).first()
        if username:
            flash('username exists')
        if email:
            flash('email exists')
        if phone:
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
            user_type=0,
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    logger.debug('login')
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if  request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember')
        logger.debug(request.form)

        user = User.query.filter_by(username=username).first()

        if user and user.status == False :
            flash('user not able use')
        if user and bcrypt.check_password_hash(user.password.encode('utf-8'), password.encode('utf-8')):
            login_user(user, True)
            return redirect(url_for('main.home'))
        else:
            flash('username or password error')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have login out')
    return redirect(url_for('auth.login'))

