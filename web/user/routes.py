from flask import render_template, url_for,Blueprint,redirect,flash,request
from flask_login import login_user, logout_user, login_required,current_user
from web import get_logger,bcrypt,db
from flask_login import login_required
from web.models import User
from web.user.forms import UserSearchForm

logger = get_logger(__name__)
user = Blueprint('user', __name__)


@user.route("/profile",methods=['POST','Get'])
@login_required
def profile():
    if current_user.is_authenticated:
        user_id = current_user.get_id()
        user = User.query.filter_by(id=user_id).first()

    return render_template('user/profile.html',user=user)


@user.route("/managment",methods=['POST','Get'])

def managment():
    form = UserSearchForm(request.form)
    user_type = None
    if current_user.is_authenticated and current_user.user_type == 1:
        print('------ {0}'.format())

        if request.form:
           user_type = form.usertype_select.data

        logger.debug(user_type)
        if user_type == None or user_type == 0:
           user_items = User.query.all()
        else:
           user_items = User.query.filter_by(user_type=user_type)
        return render_template('user/managment.html', form= form,users=user_items)

    return render_template('auth/login.html')



