from flask import render_template, url_for,Blueprint,redirect,flash,request
from flask_login import login_user, logout_user, login_required,current_user
from web import get_logger,bcrypt,db
from flask_login import login_required
from web.models import User, Quizdata, Quiztype
from web.user.forms import UserSearchForm,ResetPasswordForm

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
#@login_required
def managment():
    form = UserSearchForm(request.form)
    user_type = None
    if current_user.is_authenticated and current_user.user_type == 1:

        if request.method == "POST":
           user_type = request.form.get('usertype_select')

        logger.debug(user_type)
        if user_type == None or user_type == str(0):
           user_items = User.query.all()
        else:
           user_items = User.query.filter_by(user_type=user_type)
        return render_template('user/managment.html', form= form,users=user_items)

    elif current_user.is_authenticated and current_user.user_type == 2:
        flash("You are not Admin user")
        return redirect(url_for('main.content'))
    else:
        return redirect(url_for('auth.login'))

    return


@user.route("/user/<int:userid>/status/<int:status>",methods=['POST'])
@login_required
def user_status(userid,status):
    logger.debug("userid:" + str(userid)+" set status:" + str(status))
    user = User.query.get_or_404(userid)
    user.status = status
    db.session.commit()
    flash('user status set success','success')
    return redirect(url_for('user.managment'))


@user.route("/user/<int:userid>/reset_password",methods=['POST','GET'])
@login_required
def reset_password(userid):
    form = ResetPasswordForm()
    user = User.query.filter_by(id=userid).first()
    if  request.method == 'POST' :
        logger.debug(user)
        if user and request.form.get('password')==request.form.get('confirm_password'):
            password = request.form.get('password')
            user.password = bcrypt.generate_password_hash(password).decode('utf-8')
            logger.debug(password)
            db.session.commit()
            flash('change password success','success')

            if user.user_type == 1:
               return redirect(url_for('user.managment'))
            else:
               return redirect(url_for('auth.logout'))
        elif request.form.get('password')!=request.form.get('confirm_password') :
            flash('password and comfirm password are not same ', 'success')
        else:
            flash('change password fail')

    return render_template('user/resetpassword.html',form=form)


@user.route('/user/<int:userid>/statistic', methods=['GET', 'POST'])
#@login_required
def statistic(userid):
    users = Quizdata.query.filter_by(user_id=userid).all()
    user_list = []
    score =0
    total =0
    average_score=0
    for item in users:
        score+=item.score
        total+=1
        quiztype = Quiztype.query.filter_by(id=item.quiztype_id).first()
        user_list.append({"score": item.score,
                            "date": item.date,
                            "level": quiztype.level,
                            "topic": quiztype.topic,})
    if total > 0:
       average_score = int(score/total)
    return render_template("statistic.html", users=user_list,average_score=average_score,total=total)




