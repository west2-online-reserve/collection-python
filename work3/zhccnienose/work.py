from flask import Flask, request, jsonify, abort
from work_sql import SqlDb

# 应用对象
app = Flask(__name__)
# 初始化数据库对象
sql = SqlDb()
sql.db = sql.init_db()
# 建立游标对象
sql.cursor = sql.db.cursor()
list_key = ("id", "title", "content", "state", "add_time", "end_time")


@app.errorhandler(404)
def error_hander(e):
    return jsonify(code=404, msg="该活动不存在")


# 添加一条待办事项
@app.route("/add", methods=["POST"])
def add_task():
    data_task = request.get_json()  # 获取请求数据
    id = data_task.get("id")

    # 通过 查询id 判断是否存在
    if len(sql.query_db(id)) == 0:
        data_task = tuple(data_task.values())
        sql.ins_db(data_task)  # 添加待办事项
        return jsonify(code=200, msg="添加成功")
    else:
        abort(404)


# 修改 对应id 待办事项 完成状态
@app.route("/modify/id", methods=["POST"])
def mofity_id():
    data_task = request.get_json()
    id = data_task.get("id")
    state = data_task.get("state")
    data = query_task(id).get_json()

    if data.get("msg") is None and data.get("state") != state:
        sql.modify_db_id(id, state)
        return jsonify(code=200, msg="修改成功")

    elif data.get("msg") is not None:
        abort(404)


# 修改 所有 待办事项 完成状态
@app.route("/modify/all", methods=["POST"])
def modify_all():
    if sql.query_db_all(1, 1):
        data_task = request.get_json()
        state = data_task.get("state")
        sql.modify_db_all(state)
        return jsonify(code=200, msg="已将所有待办事项完成状态改为%s" % state)
    else:
        abort(404)


# 删除 对应id 待办事项
@app.route("/del/id", methods=["GET"])
def del_task():
    id = request.get_json().get("id")
    if query_task(id).get_json().get("msg") is None:
        sql.del_db(id)
        return jsonify(code=200, msg="该事项删除成功")
    else:
        abort(404)


# 删除 已完成 待办事项
@app.route("/del/completed", methods=["GET"])
def del_task_completed():
    # 判断是否存在 已完成事项
    if sql.query_db_completed(1, 1):
        sql.del_db_completed()
        return jsonify(msg="已完成事项删除成功")
    else:
        abort(404)


# 删除 待完成 待办事项
@app.route("/del/completing", methods=["GET"])
def del_task_completing():
    if sql.query_db_completing(1, 1):
        sql.del_db_completing()
        return jsonify(msg="待完成事项删除成功")
    else:
        abort(404)


# 删除 全部 待办事项
@app.route("/del/all", methods=["GET"])
def del_task_all():
    data_task_all = sql.query_db_all(1, 1)

    if data_task_all:
        sql.del_db_all()
        return jsonify(msg="所有事项删除成功")
    else:
        abort(404)


# 查询 对应id 的待办事项
@app.route("/query/id", methods=["POST"])
def query_task():
    id = request.get_json().get("id")
    data_query = sql.query_db(id)

    if data_query:
        data_task = dict(zip(list_key, data_query[0]))
        return jsonify(code=200, data=data_task)
    else:
        abort(404)


# 查询 对应关键字 待办事项
#
@app.route("/query/key", methods=["POST"])
def query_task_key():
    # 获取请求参数
    data_post = request.get_json()
    page = data_post.get("page")  # 页码
    pagesize = data_post.get("pagesize")  # 每页事项条数
    key = data_post.get("key")  # 关键字
    value = data_post.get("value")  # 关键字对应的值

    data_query_key = sql.query_db_key(key, value, page=page, pagesize=pagesize)

    # 判断返回数据是否为 空
    if len(data_query_key) != 0:
        data_task = {}
        num = 1  # 数据序号
        for data in data_query_key:
            data_task[str(num)] = dict(zip(list_key, data))
            num += 1

        return jsonify(code=200, data=data_task)
    else:
        abort(404)


# 查询 已完成 待办事项

@app.route("/query/completed", methods=["POST"])
def query_task_completed():
    data_page = request.get_json()
    page = data_page.get("page")  # 页码
    pagesize = data_page.get("pagesize")  # 每页事项条数

    data_query_completed = sql.query_db_completed(page=page, pagesize=pagesize)

    # 判断返回数据是否为 空
    if data_query_completed:
        data_task = {}
        num = 1  # 数据序号
        for data in data_query_completed:
            data_task[str(num)] = dict(zip(list_key, data))
            num += 1

        return jsonify(code=200, data=data_task)
    else:
        abort(404)


# 查询 待完成 待办事项
@app.route("/query/completing", methods=["POST"])
def query_task_completing():
    data_page = request.get_json()
    page = data_page.get("page")  # 页码
    pagesize = data_page.get("pagesize")  # 每页事项条数
    data_query_completing = sql.query_db_completing(page=page, pagesize=pagesize)

    # 判断返回数据是否为 空
    if data_query_completing:

        data_task = {}
        num = 1  # 数据序号
        for data in data_query_completing:
            data_task[str(num)] = dict(zip(list_key, data))
            num += 1

        return jsonify(code=200, data=data_task)
    else:
        abort(404)


# 查询 全部待办事项
# page:页码，pagesize:每页事项条数
@app.route("/query/all", methods=["POST"])
def query_task_all():
    data_page = request.get_json()
    page = data_page.get("page")  # 页码
    pagesize = data_page.get("pagesize")  # 每页事项条数
    data_query_all = sql.query_db_all(page=page, pagesize=pagesize)  # 分页查询获取的数据

    # 判断返回数据是否为 空
    if data_query_all:
        data_task = {}
        num = 1  # 数据序号
        for data in data_query_all:
            data_task[str(num)] = dict(zip(list_key, data))
            num += 1

        return jsonify(code=200, data=data_task)
    else:
        abort(404)


app.run(debug=True)

sql.close_db()
