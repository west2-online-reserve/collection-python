from flask import request, jsonify
from sqlalchemy import or_

from work_sql import db, Task
from init import app


# 添加待办事项
@app.route('/task', methods=['POST'])
def add_task():
    try:
        data = request.get_json()

        task = Task(**data)
        task.add_task()
        return jsonify(code=200, msg="添加成功"), 200
    except Exception as e:
        return jsonify(code=500, msg=str(e))


# 删除一条事项
@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task_id(id):
    try:
        if id > 0:
            task = Task.find_by_id(id)
            if task is None:
                return jsonify(code=404, msg="该事项不存在"), 404
            task.delete_task()
        else:
            return jsonify(code=400, msg="参数错误"), 400

        return jsonify(code=200, msg="删除成功")
    except Exception as e:
        return jsonify(code=500, msg=str(e)), 500


# 根据完成状态删除事项
@app.route('/task/status', methods=['DELETE'])
def delete_task_status():
    status = request.args.get('status')

    if status != "undone" and status != "done":
        return jsonify(code=400, msg="参数错误"), 400

    list_task = Task.query.filter_by(status=status).all()
    for task in list_task:
        task.delete_task()

    db.session.commit()

    return jsonify(code=200, msg="删除成功"),200


# 删除所有事项
@app.route('/task/all', methods=['DELETE'])
def delete_task_all():
    Task.query.delete()
    db.session.commit()

    return jsonify(code=200, msg="删除成功")


# 查询单条事项
@app.route('/task/<int:id>', methods=['GET'])
def get_task(id):
    try:
        if id is not None and id > 0:
            task = Task.find_by_id(id)
            if task is not None:
                return jsonify(code=200,
                               msg="success",
                               data=task.data()), 200
            else:
                return jsonify(code=400, msg="该事项不存在"), 400
    except Exception as e:
        return jsonify(code=500, msg=str(e)), 500


# 根据关键字模糊查询
@app.route('/task', methods=['GET'])
def get_task_keyword():
    keyword = request.args.get('keyword')
    # 每页数量
    per_page = request.args.get('per_page', type=int)

    # 标题或内容包含关键字
    tasks = Task.query.filter(or_(Task.title.contains(keyword), Task.content.contains(keyword)))

    cot = tasks.count()
    if cot % per_page != 0:
        pages = cot // per_page + 1
    else:
        pages = cot // per_page

    tasks = tasks.paginate(per_page=per_page, error_out=False)
    list_task = []

    for i in range(pages):
        data = tasks.items
        list_task.append([])
        for task in data:
            list_task[i].append(task.data())

        tasks = tasks.next()

    return jsonify(code=200, msg="success", data=list_task)


# 根据完成状态查询事项
@app.route('/task/status', methods=['GET'])
def get_task_status():
    # 完成状态
    status = request.args.get('status')
    if status != "undone" and status != "done":
        return jsonify(code=400, msg="参数错误"), 400
    # 每页数量
    per_page = request.args.get('per_page', type=int)

    cot = Task.query.filter_by(status=status).count()
    if cot % per_page != 0:
        pages = cot // per_page + 1
    else:
        pages = cot // per_page

    tasks = Task.query.filter_by(status=status).paginate(per_page=per_page, error_out=False)
    list_task = []

    for i in range(pages):
        data = tasks.items
        list_task.append([])
        for task in data:
            list_task[i].append(task.data())

        tasks = tasks.next()

    return jsonify(code=200, msg="success", data=list_task)


# 查询所有事项
@app.route('/task/all', methods=['GET'])
def get_task_all():
    # 每页数量
    per_page = request.args.get('per_page', type=int)

    cot = Task.query.count()
    if cot % per_page != 0:
        pages = cot // per_page + 1
    else:
        pages = cot // per_page

    tasks = Task.query.paginate(per_page=per_page, error_out=False)
    list_task = []

    for i in range(pages):
        data = tasks.items
        list_task.append([])
        for task in data:
            list_task[i].append(task.data())

        tasks = tasks.next()

    return jsonify(code=200, msg="success", data=list_task)


# 根据id更新状态
@app.route('/task/<int:id>', methods=['PUT'])
def update_task_id(id):
    task = Task.find_by_id(id)
    if id < 0:
        return jsonify(code=400, msg="参数错误"), 400
    else:
        if task.status == "undone":
            task.status = "done"
        elif task.status == "done":
            task.status = "undone"

        db.session.commit()
    return jsonify(code=200, msg="修改成功"), 200


# 根据状态更新状态
@app.route('/task/status', methods=['PUT'])
def update_task_status():
    try:
        old_status = request.args.get('old_status', type=str)
        if old_status != "undone" and old_status != "done":
            return jsonify(code=400, msg="参数错误"),400

        if old_status == "undone":
            new_status = "done"
        else:
            new_status = "undone"

        list_task = Task.query.filter_by(status=old_status).all()
        if list_task is not None:
            for task in list_task:
                task.status = new_status
        else:
            pass

        db.session.commit()
        return jsonify(code=200, msg="修改成功")
    except Exception as e:
        return jsonify(code=500, msg=str(e))


if __name__ == '__main__':
    app.run()
