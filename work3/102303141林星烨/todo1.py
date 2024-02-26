# 导入所需模块
import pymysql

pymysql.install_as_MySQLdb()  # 可以解决无法连接的问题
from flask import Flask, request, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import text


######db.session.commit（）提交数据库的修改（包括增/删/改）###########
# 创建 Flask 应用
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3308/star'  ######数据库地址######
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 创建 SQLAlchemy 实例
db = SQLAlchemy(app)


# 定义数据模型
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary_key=True可以将id栏定义为自增列
    title = db.Column(db.String(120), nullable=False)  # 使其不可标记为空 符合正常使用
    content = db.Column(db.Text, nullable=False)  # 新增文本内容
    completed = db.Column(db.String(20), nullable=False)  # 使其不可标记为空 符合正常使用 只需要false 和 true
    created_at = db.Column(db.DateTime)
    deadline = db.Column(db.DateTime)


###数据库语言###
with app.app_context():
    result = db.session.execute(text("SHOW TABLES LIKE 'todo'"))
    todo_exist = result.fetchone() is None
    if todo_exist:
        todo_exist = False
        todo1 = Todo(title='example',
                     content='example',
                     completed='true',
                     created_at=datetime.now(),
                     deadline=datetime.now())
        db.create_all()
        db.session.add(todo1)
        db.session.commit()


@app.route('/')
def index():
    results = []
    todos = Todo.query.all()
    for todo in todos:
        results.append(jsonify(title=todo.title, content=todo.content, completed=todo.completed,
                               created_at=todo.created_at, deadline=todo.deadline))
        return jsonify(code=200, message='ALL', result=results)


#####插入一条#####(增)
@app.route('/add_todo', methods=['POST'])
def add_todo():
    data = request.json
    todo_title = data['title']
    todo_complete = data['completed']
    todo_content = data['content']
    if todo_complete != 'true':
        todo_complete = 'false'
    else:
        todo_complete = 'true'
    new_todo = Todo(title=todo_title, completed=todo_complete, content=todo_content, created_at=datetime.now(),
                    deadline=datetime.now())
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(message='success', code=200)


#####将 一条/所有待办事项设置为已完成#####（改）
####一条####
@app.route('/update/<int:todo_id>', methods=["POST"])
def update(todo_id):
    need_todo = Todo.query.get(todo_id)  # 通过todo_id来找需要修改的那一条

    if need_todo is None:
        return jsonify(code=404, msg='NOT FOUND')
    else:
        need_todo.completed = 'true'
        db.session.commit()
        return jsonify(code=200, msg='update single success')


####所有####
@app.route('/update/all', methods=['POST'])
def update_all():
    need_all = Todo.query.filter_by(completed='false').all()
    for all in need_all:
        all.completed = 'true'
    db.session.commit()
    return jsonify(code=200, msg='update all success')


#####将 一条/所有事项设置为代办#####（改）
####一条####
@app.route('/update2/<int:todo_id>', methods=["POST"])
def update_2(todo_id):
    need_todo = Todo.query.get(todo_id)  # 通过todo_id来找需要修改的那一条
    if need_todo is None:
        return jsonify(code=404, msg='NOT FOUND')
    else:
        need_todo.completed = 'false'
        db.session.commit()
        return jsonify(code=200, msg='update single success')


####所有####
@app.route('/update2/all', methods=['POST'])
def update_2_all():
    need_all = Todo.query.filter_by(completed='true').all()
    for all in need_all:
        all.completed = 'false'
    db.session.commit()
    return jsonify(code=200, msg='update all success')


#####查看 所有已完成/所有待办/所有事项 （需分页）#####(查)
####查看 所有已完成####
@app.route('/search/all/completed', methods=['GET'])
def search_all_completed():
    search_all = Todo.query.filter_by(completed='true').all()
    result_data = []
    for single in search_all:
        result_data.append({'id': single.id,
                            'title': single.title,
                            'content': single.content,
                            'completed': single.completed,
                            'created_at': single.created_at,
                            'deadline': single.deadline})
    return jsonify(code=200, msg="success", data=result_data)


####查看 所有代办####
@app.route('/search/all/not_completed', methods=['GET'])
def search_all_not_completed():
    search_all = Todo.query.filter_by(completed='false').all()
    result_data = []
    for single in search_all:
        result_data.append({'id': single.id,
                            'title': single.title,
                            'completed': single.completed,
                            'created_at': single.created_at,
                            'deadline': single.deadline})
    return jsonify(code=200, msg="success", data=result_data)


####查看 所有事项####
@app.route('/search/all', methods=['GET'])
def search_all():
    search_all = Todo.query.all()
    result_data = []
    for single in search_all:
        result_data.append({'id': single.id,
                            'title': single.title,
                            'completed': single.completed,
                            'created_at': single.created_at,
                            'deadline': single.deadline})
    return jsonify(code=200, msg="success", data=result_data)


####用关键词查询####
@app.route('/search/by_kw/<kw>', methods=['GET'])
def search_by_kw(kw):
    search_kw = Todo.query.filter_by(title=kw).all()

    if search_kw is None:
        return jsonify(code=404, msg='NOT FOUND')
    else:
        datas = []
        for search_kw_ in search_kw:
            datas.append([{'id': search_kw_.id,
                           'title': search_kw_.title,
                           'completed': search_kw_.completed,
                           'created_at': search_kw_.created_at,
                           'deadline': search_kw_.deadline}])
        return jsonify(code=200, msg='search success', data=datas)


####用id查询####
@app.route('/search/by_id/<int:todo_id>', methods=['GET'])
def search_id(todo_id):
    search_single = Todo.query.get(todo_id)
    if search_single is None:
        return jsonify(code=404, msg='NOT FOUND')
    else:
        data = [{'id': search_single.id,
                 'title': search_single.title,
                 'completed': search_single.completed,
                 'created_at': search_single.created_at,
                 'deadline': search_single.deadline}]
        return jsonify(code=200, msg='search success', data=data)


#####删除 一条/所有已完成/所有待办/所有事项#####
####删除一条事项####
@app.route('/delete/single_completed/<int:todo_id>', methods=['DELETE'])
def delete_single_completed(todo_id):
    delete_single = Todo.query.get_or_404(todo_id)
    db.session.delete(delete_single)
    db.session.commit()
    return jsonify(code=200, msg='delete single success')


####删除所有事项####
@app.route('/delete/all', methods=['DELETE'])
def delete_all():
    delete_all = Todo.query.all()
    for single in delete_all:
        db.session.delete(single)
    db.session.commit()
    return jsonify(code=200, msg='delete all success')


####删除所有已完成###
@app.route('/delete/all_completed', methods=['DELETE'])
def delete_all_completed():
    delete_all = Todo.query.filter_by(completed='true').all()
    for single in delete_all:
        db.session.delete(single)
    db.session.commit()
    return jsonify(code=200, msg='delete all completed success')


####删除所有代办###
@app.route('/delete/all_not_completed', methods=['DELETE'])
def delete_all_not_completed():
    delete_all = Todo.query.filter_by(completed='false').all()
    for single in delete_all:
        db.session.delete(single)
    db.session.commit()
    return jsonify(code=200, msg='delete all not completed success')


if __name__ == '__main__':
    app.run(debug=True)
