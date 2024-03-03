import timestamp
from flask import Flask
import pymysql
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:666666@127.0.0.1:3306/test'

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + "/home/lmp/sql/sec.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "jjjsks"

db = SQLAlchemy(app)  # 实例化的数据库


class ToDoList(db.Model):
    __tablename__ = "todo_list"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(32), nullable=False)
    content = db.Column(db.String(64), nullable=False)
    state = db.Column(db.String(10),default='待办')
    create_time = db.Column(db.DateTime, default=datetime.now)
    deadline = db.Column(db.TIMESTAMP, nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        #db.drop_all()