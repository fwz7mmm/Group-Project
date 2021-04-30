from flask import render_template, url_for,Blueprint,redirect,flash
from flask_login import login_user, logout_user, login_required,current_user
from web import get_logger,bcrypt,db
from flask_login import login_required
from web.auth.forms import RegisterForm
from web.models import User
logger = get_logger(__name__)
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route("/register",methods=['GET','POST'])
#@login_required
def register():
    form = RegisterForm()
    logger.debug("here")
    if form.validate_on_submit():
        logger.debug("h")
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
        username = form.username.data,
        email=form.email.data,
        password=hashed_password,
        phone = db.Column(db.Integer),
        birth = form.birth.data,
        status = True,
        )
        db.session.add(user)
        db.session.commit()
        flash('success!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html',  form=form)


@auth.route('/login', methods=['GET', 'POST'])
def LoginForm():
    logger.debug('login')
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(username=form.username.data).first()
            logger.debug(user.password)
            if user and user.status == False :
                flash('user not able use')
                return render_template('main.home', form=form)
            if user and bcrypt.check_password_hash(user.password.encode('utf-8'), form.password.data.encode('utf-8')):
                login_user(user, form.rememberme.data)
                return redirect(url_for('main.index'))
            else:
                flash('username or password error')
        except Exception as e:
            logger.debug(e)
            flash('error')
    return render_template('login.html', form=form)

