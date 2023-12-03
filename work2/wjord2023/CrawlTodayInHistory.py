import re
import warnings

import mysql.connector
import requests
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning

if __name__ == "__main__":
    # 连接mysql数据库
    conn = mysql.connector.connect(host='localhost', user='root', password='102302', database='MyDepository')
    cursor = conn.cursor()

    truncate_table_query = "DROP TABLE IF EXISTS TodayInHistory "
    cursor.execute(truncate_table_query)
    # 创建数据表
    cursor.execute('''
               CREATE TABLE IF NOT EXISTS TodayInHistory(
                   `id` INT AUTO_INCREMENT PRIMARY KEY,
                   `year` VARCHAR(5),
                   `type` VARCHAR(25),
                   `title` TEXT,
                   description TEXT
               )
       ''')
    # 打印的时候会出现这个报错虽然没什么影响但很烦就把它禁用了
    warnings.simplefilter("ignore", MarkupResemblesLocatorWarning)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    # 观察json格式发现可以用json[01][0131][序号]这样的格式查找每月每天每一条，于是写了一个循环来导入参数
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(1, 13):
        mon = '{:02d}'.format(i)
        url = 'https://baike.baidu.com/cms/home/eventsOnHistory/' + str(mon) + '.json?_=1697897224157'
        response = requests.get(url, headers)
        response_json = response.json()
        for j in range(1, days[i - 1] + 1):
            day = '{:02d}'.format(j)
            len_info = len(response_json[str(mon)][str(mon) + str(day)])
            for l in range(0, len_info - 1):
                year = response_json[str(mon)][str(mon) + str(day)][l]['year'].strip()
                type = response_json[str(mon)][str(mon) + str(day)][l]['type'].strip()
                desc_html_ = response_json[str(mon)][str(mon) + str(day)][l]['desc'].strip()
                title_html_ = response_json[str(mon)][str(mon) + str(day)][l]['title'].strip()
                soup_title = BeautifulSoup(title_html_, 'html.parser')
                soup_desc = BeautifulSoup(desc_html_, 'html.parser')
                # 用re保证不会有换行符
                title = re.sub(r'\s+', '', soup_title.get_text().strip())
                desc = re.sub(r'\s+', '', soup_desc.get_text().strip())
                print(year, type, title, desc)
                cursor.execute('''
                                            INSERT INTO TodayInHistory (year,type,title,description)
                                            VALUES (%s, %s, %s, %s)
                                        ''', (year, type, title, desc))

    conn.commit()
    conn.close()
