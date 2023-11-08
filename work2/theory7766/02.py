import time
import calendar
import requests
import re
import json
from pymysql import Connection

def process(num):
    if num < 10:
        return "0"+str(num)
    else:
        return str(num)

# 创建表
def createTable():
    con = None
    try:
        con = Connection(
            host="localhost",  # 主机名
            port=3306,  # 端口
            user="root",  # 用户名
            password="Lucy0311@",  # 密码
            database="db1",  # 指定操作的数据库
            autocommit=True
        )
        # 若未在数据库db1中创建表events则创建
        createEventsSql = """
                            CREATE TABLE IF NOT EXISTS `events` (
                            `year` VARCHAR (6) NOT NULL ,
                            `date` VARCHAR (6) NOT NULL ,
                            `title` VARCHAR (200) NOT NULL ,
                            `type` VARCHAR(10) NOT NULL,
                            `desc` VARCHAR (1000) NOT NULL
                            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
                         """
        cursor = con.cursor()
        cursor.execute(createEventsSql)
        # 删除原有数据
        deleteSql = "DELETE FROM `events`"
        cursor.execute(deleteSql)
    except Exception as e:
        print("异常1：", e)
    finally:
        if con:
            con.close()

def crawData(month,url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    html = response.json()
    # 存该月份对应的数据
    month_list = []
    for day in range(1, calendar.monthlen(2023, int(month)) + 1):
        day = process(day)
        events = html[month][month+day]
        for j in range(len(events)):
            year = events[j]['year'].replace('\n', '')
            type = events[j]['type']
            title = events[j]['title']
            desc = events[j]['desc'].replace('\n', '')
            title = re.sub(r'<.*?>', '', title) # 除去标题中的超链接
            desc = re.sub(r'<.*?>', '', desc) # 除去描述中的超链接
            temp = {'year': year, 'date': month+'.'+day, 'type': type, 'title': title, 'desc': desc}
            month_list.append(temp)
    return month_list

def insertDb(info_list):
    # 创建数据库链接
    con = None
    try:
        con = Connection(
            host="localhost",  # 主机名
            port=3306,  # 端口
            user="root",  # 用户名
            password="Lucy0311@",  # 密码
            database="db1",  # 指定操作的数据库
            autocommit=True  # insert时使用
        )
        insertEventsSql = "INSERT INTO `events`(`year`,`date`,`type`,`title`,`desc`) VALUES (%s, %s, %s, %s, %s);"
        cursor = con.cursor()
        for info in info_list:
            print(json.dumps(info, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':')))
            cursor.execute(insertEventsSql, (info['year'], info['date'], info['type'], info['title'], info['desc']))
        cursor.close()
    except Exception as e:
        print("异常2：", e)
        # print(json.dumps(info, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':')))
    finally:
        if con:
            con.close()

def main():
    # 建表
    createTable()
    for month in range(1, 13):
        month = process(month)
        url = "https://baike.baidu.com/cms/home/eventsOnHistory/"+month+".json?_="+str(time.time())
        events_list = crawData(month, url)
        # 立刻将该月数据存入数据库
        insertDb(events_list)

if __name__=='__main__':
    main()
