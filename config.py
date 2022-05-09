import os
import keyring
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    db_username = 'cat_dba'
    db_password = keyring.get_password('cat_db', 'cat_dba')
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + db_username + ': ' + db_password + '@localhost:5432/cat_db'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
