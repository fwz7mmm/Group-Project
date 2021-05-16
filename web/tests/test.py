import unittest, os
from web import app, db,create_app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from web.models import User, Quiztype, Questions, Quizdata
TEST_DB = 'test.db'

db = SQLAlchemy()
app = Flask(__name__)
migrate = Migrate()
#https://www.patricksoftwareblog.com/unit-testing-a-flask-application/
class WebModelCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../test.db'
        self.app=app.test_client()
        db.init_app(app)
        with app.app_context():
             db.create_all()
        user1 = User(id='0', username='parker', email='parker@gmail',password='p12345', phone='060502548',birth='25/15/2015', status=0, user_type='0')
        db.session.add(user1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_is_commut(self):
        s = User.query.get('0')
        self.assertEqual(s.username, 'parker')

    if __name__ == "__main__":

        unittest.main()

    
