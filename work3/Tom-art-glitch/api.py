from flask import jsonify, request, session

from models import app, db, ToDoList
import datetime

#初始页
@app.route("/index", methods=["GET"])
def hel():
    return 'Hello world!'

#添加待办
@app.route("/create", methods=["POST"])
def create():
    req_data = request.get_json()
    title = req_data.get("title")
    content = req_data.get("content")
    deadline = datetime.datetime.strptime(req_data.get("deadline"), '%Y-%m-%d %H:%M:%S')

    if not all([title, content,deadline]):
        return jsonify(code=400, msg="参数不完整")

    try:
        todolist = ToDoList(title=title, content=content, deadline=deadline)
        db.session.add(todolist)
        db.session.commit()
        return jsonify(code=200, msg="添加待办成功")

    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="添加待办失败")

#删除待办
@app.route("/drop", methods=["DELETE"])
def drop():
    req_data = request.get_json()
    i_d = req_data.get("id")

    if not all([i_d]):
        return jsonify(code=400, msg="参数不完整")

    # 判断待办存在
    do_id = ToDoList.query.get(i_d)
    if do_id is None:
        return jsonify(code=400, msg="待办不存在，无法完成删除操作")
    try:
        m = ToDoList.query.filter(ToDoList.id == i_d).first()
        db.session.delete(m)
        db.session.commit()
        return jsonify(code=200, msg="删除成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="删除失败")

#删除多条待办
@app.route("/dropsome", methods=["DELETE"])
def drops():
    req_data = request.get_json()
    state = req_data.get("state")
    if not all([state]):
        todos = ToDoList.query.filter(ToDoList.id !=0).all()
    # 判断待办存在
    else:
        todos = ToDoList.query.filter(ToDoList.state == state).all()
    if len(todos) == 0:
        return jsonify(code=400, msg="待办不存在，无法完成删除操作")
    try:
        for todo in todos:
            db.session.delete(todo)
        db.session.commit()
        return jsonify(code=200, msg="删除成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="删除失败")
#查询待办
@app.route("/look", methods=["POST"])
def look():
    req_data = request.get_json()
    page = req_data.get('page')
    state = req_data.get('state')
    key_word = req_data.get("keyword")
    if page is None:
        page = 1
    else:
        page = int(page)
    if all([key_word, state]):
        todolists = ToDoList.query.filter(ToDoList.title.contains(key_word)).filter(ToDoList.state == state).paginate(page=page, per_page=5, error_out=False)
    elif not(state is None):
        todolists = ToDoList.query.filter(ToDoList.state == state).paginate(page=page, per_page=5, error_out=False)
    elif not(key_word is None):
        todolists = ToDoList.query.filter(ToDoList.title.contains(key_word)).paginate(page=page, per_page=5, error_out=False)
    else:
        todolists = ToDoList.query
    payload = []
    for todolist in todolists:
        do_id = todolist.id
        content = todolist.content
        title = todolist.title
        deadline = todolist.deadline
        state = todolist.state
        create_time = todolist.create_time.strftime("%Y-%m-%d %H:%M:%S")
        data = {"content": content,
                'title': title,
                "id": do_id,
                "state": state,
                "create_time": create_time,
                'deadline': deadline}
        payload.append(data)
    return jsonify(code=200, msg="查询成功", data=payload)

#修改某条待办状态
@app.route("/update", methods=["PUT"])
def update():
    req_data = request.get_json()
    i_d = req_data.get('id')
    new_state = req_data.get('state')

    if not all([i_d, new_state]):
        return jsonify(code=400,msg='参数不完整')

    do_id = ToDoList.query.get(i_d)
    if do_id is None:
        return jsonify(code=400, msg="待办不存在，无法完成更新操作")

    try:
        ToDoList.query.filter(ToDoList.id == i_d).update({'state': new_state})

        db.session.commit()
        return jsonify(code=200, msg='更改成功')
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg='更改失败')

#修改多条待办状态
@app.route("/updateall", methods=["PUT"])
def updateall():
    req_data = request.get_json()
    new_state = req_data.get('state')

    if not all([new_state]):
        return jsonify(code=400,msg='参数不完整')

    todos = ToDoList.query.filter(ToDoList.id != 0).all()

    try:
        for todo in todos:
            ToDoList.query.filter(ToDoList.id == todo.id).update({'state': new_state})
        db.session.commit()
        return jsonify(code=200, msg='更改全部成功')
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg='更改失败')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5050)