import os

class Configuration(object):
    DEBUG = True
    PORT = int(os.environ['PORT'])
    HOST = '0.0.0.0'
    DB_USER = os.environ["MYSQLCS_USER_NAME"]
    DB_PWD = os.environ["MYSQLCS_USER_PASSWORD"]
    DB_CONNECT_STR = os.environ["MYSQLCS_CONNECT_STRING"]

