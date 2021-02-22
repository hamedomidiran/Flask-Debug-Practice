from dotenv import load_dotenv
import os
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# Windows = Documents\codingtemple-may2020\week5\in-class\
# Mac & Linux = Documents/codingtemple-may2020/week5/in-class/jjjj

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess...'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# basedir = os.path.abspath(os.path.dirname(__name__))
# load_dotenv(os.path.join(basedir, '.env'))


# class Config:
#     SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
#     SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
#         'SQLALCHEMY_TRACK_MODIFICATIONS')
#     FLASK_APP = os.getenv('FLASK_APP')
#     FLASK_ENV = os.getenv('FLASK_ENV')
#     SECRET_KEY = os.getenv('SECRET_KEY')
#     MAIL_SERVER = os.getenv('MAIL_SERVER')
#     MAIL_PORT = os.getenv('MAIL_PORT')
#     MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
#     MAIL_USERNAME = os.getenv('MAIL_USERNAME')
#     MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
