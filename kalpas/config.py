import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = \
            os.environ.get('SQLALCHEMY_DATABASE_URI') \
            or 'sqlite:////tmp/app.db'

