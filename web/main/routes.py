from flask import Flask,render_template, url_for,session,Blueprint,request,redirect,json,flash
from web import get_logger,bcrypt,db
from web.models import Questions,Quiztype,Quizdata
from flask_login import login_user, logout_user, login_required,current_user
from datetime import datetime
logger = get_logger(__name__)
main = Blueprint('main', __name__)
from flask_login import login_required
@main.route('/')
def index():
    return render_template('index.html')

@main.route("/home")
def home():
    return render_template("home.html")

@main.route("/content")
def content():
    return render_template("content.html")  

@main.route('/test', methods=['GET', 'POST'])
#@login_required
def test():
    if request.method == "POST":
        topic = request.form.get('topic')
        level = request.form.get('level')
        return redirect(url_for('main.quiz', topic=topic, level=level))

    return render_template("test.html")


@main.route('/result', methods=['GET', 'POST'])
#@login_required
def result():
    result = request.args['result']
    mark = request.args['mark']
    #cookies
    test_result = session['test_result']
    return render_template("result.html",result=json.loads(result),mark=mark)

@main.route('/quiz/<topic>,<level>', methods=['GET', 'POST'])
#@login_required
def quiz(topic, level):
    quiztype = Quiztype.query.filter_by(topic=topic,level=level).first()
    quizs  =Questions.query.filter_by(quiztype_id=quiztype.id).all()
    if request.method == "POST":

        correct=0
        total=0
        result_list=[]
        # logger.debug(request.form)
        answers = json.loads(request.form.get('answers'))
        #answers =json.loads(str('[{"questionId":"1","answer":"B: yes"},{"questionId":"2","answer":"D: oijo"},{"questionId":"3","answer":"A: mark"}]'))
        if answers:
            for item in answers:
                total+=1
                questionId=item["questionId"]
                question = Questions.query.filter_by(id=questionId).first()
                if question.answer == item["answer"]:
                    status = 1
                    correct+=1
                else:
                    status = 0
                result_list.append({"question":question.question,
                                    "choiceA":question.choiceA,
                                    "choiceB": question.choiceB,
                                    "choiceC": question.choiceC,
                                    "choiceD": question.choiceD,
                                    "answer":question.answer,
                                    "useranswer": item["answer"],
                                    "status": status})
                
            #logger.debug(result_list)
            #logger.debug(int(correct/total*100))
            mark=int(correct/total*100)
            result = json.dumps(result_list)
            # cookies
            session['test_result'] = result
            # add new quiz data
            quizdata = Quizdata(
                user_id= current_user.id,
                quiztype_id = quiztype.id,
                score = mark,
                date = str(datetime.now()),
            )
            db.session.add(quizdata)
            db.session.commit()
            return redirect(url_for('main.result', result=result, mark=mark))
        else:
            flash("error")

    return render_template("quiz.html", quizs=quizs)


@main.route('/statistic', methods=['GET', 'POST'])
#@login_required
def statistic():
    users = Quizdata.query.filter_by(user_id=current_user.id).all()
    user_list = []
    score =0
    total =0
    for item in users:
        score+=item.score
        total+=1
        quiztype = Quiztype.query.filter_by(id=item.quiztype_id).first()
        user_list.append({"score": item.score,
                            "date": item.date,
                            "level": quiztype.level,
                            "topic": quiztype.topic,})

    average_score = int(score/total)
    return render_template("statistic.html", users=user_list,average_score=average_score,total=total)