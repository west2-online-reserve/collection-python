from flask import Flask, jsonify, request, abort
import pymysql

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.errorhandler(404)
def handle_not_found_error(error):
    return jsonify({'error': error.description}), 404

@app.errorhandler(400)
def handle_bad_request_error(error):
    return jsonify({'error': error.description}), 400

@app.route('/to-do/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='to-do')
    cursor = db.cursor()
    sql = f"SELECT id,title,content,state,time,ddl FROM tasks"
    cursor.execute(sql)
    tasks = cursor.fetchall()
    db.close()
    if all(task == (None) for task in tasks) == False:
        return jsonify({'tasks': tasks}), 200
    else:
        abort(404, description='Tasks not found')

@app.route('/to-do/api/v1.0/tasks/done', methods=['GET'])
def get_tasks_done():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='to-do')
    cursor = db.cursor()
    sql = f"SELECT id,title,content,state,time,ddl FROM tasks WHERE state = 'Done'"
    cursor.execute(sql)
    tasks = cursor.fetchall()
    db.close()
    if all(task == (None) for task in tasks) == False:
        return jsonify({'tasks': tasks}), 200
    else:
        abort(404, description='Tasks not found')

@app.route('/to-do/api/v1.0/tasks/not-started', methods=['GET'])
def get_tasks_notstarted():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='to-do')
    cursor = db.cursor()
    sql = f"SELECT id,title,content,state,time,ddl FROM tasks WHERE state = 'Not started'"
    cursor.execute(sql)
    tasks = cursor.fetchall()
    db.close()
    if all(task == (None) for task in tasks) == False:
        return jsonify({'tasks': tasks}), 200
    else:
        abort(404, description='Tasks not found')

@app.route('/to-do/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='to-do')
    cursor = db.cursor()
    sql = f"SELECT id,title,content,state,time,ddl FROM tasks WHERE id = {task_id}"
    cursor.execute(sql)
    task = cursor.fetchone()
    db.close()
    if task != None:
        return jsonify({'id': task[0], 'title': task[1], 'content': task[2], 'state': task[3], 'time': task[4], 'ddl': task[5]}), 200
    else:
        abort(404, description='Task not found')

@app.route('/to-do/api/v1.0/tasks/search', methods=['POST'])
def search_task():
    if not request.json or not 'keyword' in request.json:
        abort(400, description='Bad request')
    keyword=request.json.get('keyword', "")
    if not keyword  == "":
        db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='to-do')
        cursor = db.cursor()
        sql = f"SELECT id,title,content,state,time,ddl FROM tasks WHERE title LIKE '%{keyword}%'"
        cursor.execute(sql)
        tasks = cursor.fetchall()
        db.close()
        if all(task == (None) for task in tasks) == False:
            return jsonify({'tasks': tasks}), 200
        else:
            abort(404, description='Tasks not found')
    else:
        abort(400, description='Bad request')

@app.route('/to-do/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400, description='Bad request')
    task = {
        'title': request.json.get('title', ""),
        'content': request.json.get('content', ""),
        'state': request.json.get('state', ""),
        'time': request.json.get('time', ""),
        'ddl': request.json.get('ddl', "")
    }
    if task['title'] == "":
        abort(400, description='Bad request')
    if not (task['state'] == "Done" or task['state'] == "Not started"):
        abort(400, description='Bad request')
    if task['time'] == "":
        task['time'] = "Not set"
    if task['ddl'] == "":
        task['ddl'] = "Not set"
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='to-do')
    cursor = db.cursor()
    sql = f"INSERT INTO tasks(title,content,state,time,ddl) VALUES ('{task['title']}','{task['content']}','{task['state']}','{task['time']}','{task['ddl']}')"
    cursor.execute(sql)
    db.commit()
    db.close()
    return jsonify({'task': task}), 201

@app.route('/to-do/api/v1.0/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    if not request.json:
        abort(400, description='Bad request')
    task = {
        'state': request.json.get('state', "")
    }
    if not (task['state'] == "Done" or task['state'] == "Not started"):
        abort(400, description='Bad request')
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='to-do')
    cursor = db.cursor()
    sql = f"UPDATE tasks SET state = '{task['state']}' WHERE id = {task_id}"
    cursor.execute(sql)
    db.commit()
    db.close()
    return jsonify({'task': task}), 201

@app.route('/to-do/api/v1.0/tasks/done', methods=['PATCH'])
def update_tasks_done():
    if not request.json:
        abort(400, description='Bad request')
    task = {
        'state': request.json.get('state', "")
    }
    if not (task['state'] == "Not started"):
        abort(400, description='Bad request')
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='to-do')
    cursor = db.cursor()
    sql = f"UPDATE tasks SET state = '{task['state']}' WHERE state = 'Done'"
    cursor.execute(sql)
    db.commit()
    db.close()
    return jsonify({'task': task}), 201

@app.route('/to-do/api/v1.0/tasks/not-started', methods=['PATCH'])
def update_tasks_notstarted():
    if not request.json:
        abort(400, description='Bad request')
    task = {
        'state': request.json.get('state', "")
    }
    if not (task['state'] == "Done"):
        abort(400, description='Bad request')
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='to-do')
    cursor = db.cursor()
    sql = f"UPDATE tasks SET state = '{task['state']}' WHERE state = 'Not started'"
    cursor.execute(sql)
    db.commit()
    db.close()
    return jsonify({'task': task}), 201

@app.route('/to-do/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='to-do')
    cursor = db.cursor()
    sql = f"SELECT id,title,content,state,time,ddl FROM tasks WHERE id = {task_id}"
    cursor.execute(sql)
    task = cursor.fetchone()
    if task != None:
        sql = f"DELETE FROM tasks WHERE id = {task_id}"
        cursor.execute(sql)
        db.commit()
        db.close()
        return '', 204
    else:
        abort(404, description='Task not found')

@app.route('/to-do/api/v1.0/tasks/done', methods=['DELETE'])
def delete_tasks_done():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='to-do')
    cursor = db.cursor()
    sql = f"DELETE FROM tasks WHERE state = 'Done'"
    cursor.execute(sql)
    db.commit()
    db.close()
    return '',204

@app.route('/to-do/api/v1.0/tasks/not-started', methods=['DELETE'])
def delete_tasks_notstarted():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='to-do')
    cursor = db.cursor()
    sql = f"DELETE FROM tasks WHERE state = 'Not started'"
    cursor.execute(sql)
    db.commit()
    db.close()
    return '',204

@app.route('/to-do/api/v1.0/tasks', methods=['DELETE'])
def delete_tasks():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='to-do')
    cursor = db.cursor()
    sql = f"DELETE FROM tasks"
    cursor.execute(sql)
    db.commit()
    db.close()
    return jsonify({'message': 'deleted'}), 200
    
if __name__ == '__main__':
    app.run(debug=True)