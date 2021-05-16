import unittest, os
from web import app,test_app,bcrypt
from web.models import User, Quiztype, Questions, Quizdata
from flask_sqlalchemy import SQLAlchemy


app,db=test_app()
#https://www.patricksoftwareblog.com/unit-testing-a-flask-application/
class WebModelCase(unittest.TestCase):

    def setUp(self):

        self.app=app.test_client()
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

    def tearDown(self):
        #with app.app_context():
        #db.session.remove()
        #db.drop_all()
        return

    def test_is_commut(self):
        with app.app_context():
             s = User.query.get('0')
        self.assertEqual(s.username, 'parker')

