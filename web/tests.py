import unittest, os
from web import app, db
from web.models import User, Quiztype, Questions, Quizdata

class WebModelCase(unittest, TestCase):

    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI']=\
            'sqlite:///'+os.path.join(basedir, 'test.db')
        self.app=app.test_client()
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

    
