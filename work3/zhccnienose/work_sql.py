import pymysql


class SqlDb:

    def __init__(self):
        self.db = None
        self.cursor = None

    # 连接数据库
    def init_db(self):
        self.db = pymysql.connect(host="localhost",
                                  user="root",
                                  password="C310257813.",
                                  database="WORK")

        self.cursor = self.db.cursor()

        sql_table = "DROP TABLE IF EXISTS TASK"
        self.cursor.execute(sql_table)

        self.cursor.execute("""CREATE TABLE TASK (
                                ID INT NOT NULL,
                                TITLE VARCHAR(64) NOT NULL,
                                CONTENT TEXT NOT NULL,
                                STATE VARCHAR(64) NOT NULL,
                                ADD_TIME INT NOT NULL,
                                END_TIME INT NOT NULL)""")
        self.db.commit()
        return self.db

    # 添加 事项
    def ins_db(self, data_task):
        ins_task = "INSERT INTO `TASK` (`ID`,`TITLE`,`CONTENT`,`STATE`,`ADD_TIME`,`END_TIME`) VALUES(%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(ins_task, data_task)
        self.db.commit()

    # 修改 对应id  事项 完成状态
    def modify_db_id(self, id, state):
        modify_task = f"UPDATE `TASK` SET STATE='{state}' WHERE ID='{id}'"
        self.cursor.execute(modify_task)
        self.db.commit()

    # 修改 所有  事项 完成状态
    # state:完成状态
    def modify_db_all(self, state):
        modify_task_all = f"UPDATE `TASK` SET STATE='{state}'"
        self.cursor.execute(modify_task_all)
        self.db.commit()

    # 删除 对应id  事项
    def del_db(self, id):
        del_task = "DELETE * FROM TASK WHERE ID = %s" % id
        self.cursor.execute(del_task)
        self.db.commit()

    # 删除 已完成  事项
    def del_db_completed(self):
        del_task_ted = "DELETE FROM TASK WHERE STATE = 'completed'"
        self.cursor.execute(del_task_ted)
        self.db.commit()

    # 删除 待完成 事项
    def del_db_completing(self):
        del_task_ting = "DELETE FROM TASK WHERE STATE = 'completing'"
        self.cursor.execute(del_task_ting)
        self.db.commit()

    # 删除 所有  事项
    def del_db_all(self):
        del_task_all = "DELETE * FROM TASK"
        self.cursor.execute(del_task_all)
        self.db.commit()

    # 查询 对应id  事项
    def query_db(self, id):
        query_task = "SELECT * FROM TASK WHERE ID = %s" % id
        self.cursor.execute(query_task)
        return self.cursor.fetchall()

    # 查询 已完成  事项
    # page:页码, pagesize:每页事项条数
    def query_db_completed(self, page, pagesize):
        query_task_completed = "SELECT * FROM TASK WHERE STATE = 'completed' LIMIT %s,%s"
        self.cursor.execute(query_task_completed, ((page - 1) * pagesize, pagesize))
        return self.cursor.fetchall()

    # 查询 待完成  事项
    # page: 页码, pagesize: 每页事项条数
    def query_db_completing(self, page, pagesize):
        query_task_completing = "SELECT * FROM TASK WHERE STATE = 'completing' LIMIT %s,%s"
        self.cursor.execute(query_task_completing, ((page - 1) * pagesize, pagesize))
        return self.cursor.fetchall()

    # 查询 相应关键字  事项

    def query_db_key(self, key, value, page, pagesize):
        query_task_key = "SELECT * FROM TASK WHERE %s = '%s'  LIMIT %s,%s" % (
        key, value, (page - 1) * pagesize, pagesize)
        self.cursor.execute(query_task_key)
        return self.cursor.fetchall()

    # 查询 所有 事项（分页）
    # page:页码，pagesize:每页事项条数
    def query_db_all(self, page, pagesize):
        # 分页查询
        query_task_all = "SELECT * FROM TASK LIMIT %s,%s"
        self.cursor.execute(query_task_all, ((page - 1) * pagesize, pagesize))
        return self.cursor.fetchall()

    # 关闭数据库
    def close_db(self):
        self.cursor.close()
        self.db.close()
