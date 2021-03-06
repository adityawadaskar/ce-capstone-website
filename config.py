import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ce-capstone-2020'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FREEZER_RELATIVE_URLS = False
    # FREEZER_BASE_URL = "http://localhost:8000/capstone/" # For local testing
    FREEZER_BASE_URL = "https://www.ece.ucsb.edu/~yoga/capstone/" # For deployment
