from flask import render_template, url_for,Blueprint,redirect,flash,request
from flask_login import login_user, logout_user, login_required,current_user
from web import get_logger,bcrypt,db
from flask_login import login_required
from web.models import User

logger = get_logger(__name__)
user = Blueprint('user', __name__)


@user.route("/profile",methods=['POST','Get'])
#@login_required
def profile():

    return render_template('user/profile.html')



