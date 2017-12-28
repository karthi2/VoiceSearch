import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config (object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"

    # Set the path to the database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')

    # No need to signal the app everytime a change is about to be made to the
    # database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

