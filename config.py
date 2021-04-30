import os
basedir = os.path.abspath(os.path.dirname(__file__))
import sqlite3
SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'



#class Config(object):
    # Creation of secret key for WTForms
    #SECRET_KEY = os.environ.get('SERCRET_KEY') or "123-key"
    # Set specs for SQLAlchemy
   #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
   # SQLALCHEMY_TRACK_MODIFICATIONS = False