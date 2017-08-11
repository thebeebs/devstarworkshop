import os

class Configuration(object):
    DEBUG = True
    PORT = int(os.environ['PORT'])
    HOST = '0.0.0.0'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://' \
            + os.environ['MYSQLCS_USER_NAME'] + ':' \
            + os.environ['MYSQLCS_USER_PASSWORD'] + '@' \
            + os.environ['MYSQLCS_CONNECT_STRING']
