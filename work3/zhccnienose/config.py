class Config(object):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:C310257813.@127.0.0.1:3306/todolist"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
