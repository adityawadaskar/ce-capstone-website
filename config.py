import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ce-capstone-2020'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLATPAGES_AUTO_RELOAD = DEBUG
    FLATPAGES_EXTENSION = ".md"