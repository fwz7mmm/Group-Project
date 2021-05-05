from flask import Flask,render_template, url_for,session,Blueprint,request,redirect,json,flash
from web import get_logger,bcrypt,db
from web.models import Questions,Quiztype

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
                result_list.append({"question":question.question,
                                    "choiceA":question.choiceA,
                                    "choiceB": question.choiceB,
                                    "choiceC": question.choiceC,
                                    "choiceD": question.choiceD,
                                    "answer":question.answer,
                                    "useranswer": item["answer"]})
                if question.answer == item["answer"]:
                    correct+=1
            logger.debug(result_list)
            logger.debug(int(correct/total*100))
            result = json.dumps(result_list)
            # cookies
            session['test_result'] = result
            return redirect(url_for('main.result', result=result, mark=int(correct/total*100)))
        else:
            flash("error")

    return render_template("quiz.html", quizs=quizs)