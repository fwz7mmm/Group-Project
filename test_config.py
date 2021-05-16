import os
basedir = os.path.abspath(os.path.dirname(__file__))

TESTING=True
DEBUG = False
# information about databse setup
SQLALCHEMY_DATABASE_URI = 'sqlite:///../test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'

# information about email setup
MAIL_SERVER='smtp.gmail.com'
MAIL_PORT= 465
MAIL_USERNAME= 'wenwuw121wwwww@gmail.com'
MAIL_PASSWORD= 'w121wwwww'
MAIL_USE_TLS= False
MAIL_USE_SSL= True