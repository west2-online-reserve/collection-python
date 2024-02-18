from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from init import db


class Task(db.Model):
    __tablename__ = 'todolist'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    add_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    def data(self):
        return {"id": self.id,
                "title": self.title,
                "content": self.content,
                "status": self.status,
                "add_time": self.add_time,
                "end_time": self.end_time}

    # 添加待办事项
    def add_task(self):
        db.session.add(self)
        db.session.commit()

    # 删除待办事项
    def delete_task(self):
        db.session.delete(self)
        db.session.commit()

    # 更新完成状态
    def update_status(self, status):
        self.status = status
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
