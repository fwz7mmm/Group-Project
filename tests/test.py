import unittest, os
from web import app,test_app,bcrypt
from web.models import User, Quiztype, Questions, Quizdata
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required,current_user


app,db=test_app()
#https://www.patricksoftwareblog.com/unit-testing-a-flask-application/
class WebModelCase(unittest.TestCase):

    def setUp(self):

        self.app=app.test_client()


    def tearDown(self):
        with app.app_context():
             db.session.remove()
             User.query.delete()
             Quiztype.query.delete()
             Questions.query.delete()
             Quizdata.query.delete()
             db.session.commit()
        return


    def test_new_user(self):
        hashed_password = bcrypt.generate_password_hash("p12345").decode('utf-8')
        user = User(
            username='parker',
            email='parker@gmail',
            password=hashed_password,
            phone='060502548',
            birth='25/15/2015',
            status=1,
            user_type=2,
        )
        with app.app_context():
            db.session.add(user)
            db.session.commit()
            s = User.query.filter_by(username="parker").first()
        self.assertEqual(s.username, 'parker')


    def test_new_quiztype(self):
        quiztype = Quiztype(
            level = "test",
            topic = "test",
        )
        with app.app_context():
            db.session.add(quiztype)
            db.session.commit()
            s = Quiztype.query.filter_by(id=1).first()
        self.assertEqual(s.level, 'test')


    def test_new_questions(self):
        question = Questions(
              question = "test",
              choiceA = "test",
              choiceB = "test",
              choiceC  = "test",
              choiceD  = "test",
              answer  = "test",
              quiztype_id = 1,
        )
        with app.app_context():
            db.session.add(question)
            db.session.commit()
            s = Questions.query.filter_by(id=1).first()
        self.assertEqual(s.question, 'test')



    def test_new_quizdata(self):
            quizdata = Quizdata(

                    user_id = 1,
                    quiztype_id = 1,
                    score = 30,
                    date = "today",
            )
            with app.app_context():
                db.session.add(quizdata)
                db.session.commit()
                s = Quizdata.query.filter_by(id=1).first()
            self.assertEqual(s.date, 'today')

        # user name and password correct
    def test_identical_name_password(self):
        hashed_password = bcrypt.generate_password_hash("p123456").decode('utf-8')
        user = User(
            username='parker1',
            email='parker@gmail.com',
            password=hashed_password,
            phone='060502538',
            birth='25/15/2015',
            status=1,
            user_type=2,
        )
        with app.app_context():
            db.session.add(user)
            db.session.commit()
        with self.app:
            self.app.post("/login", data={"username": "parker1", "password": "p123456"})
            self.assertEqual(current_user.id, 1)


        # user name and password resgieser
    def test_identical_name_password(self):
        with self.app:
            self.app.post("/register", data={"username": "parker2","password": "p1234568","email":'parker@gmail1.com',"phone":'160502538',"birth":'25/15/2015',})
        with app.app_context():
            s = User.query.filter_by(username="parker2").first()
        self.assertEqual(s.username, 'parker2')
