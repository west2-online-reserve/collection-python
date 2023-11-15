import json
from jsonpath import jsonpath
import requests
import re
import pymysql

if __name__ == '__main__':
    # 创建连接
    try:
        connection = pymysql.connect(host='127.0.0.1', user='root', password='DHcyz20040310', db='dbtest')

        # 创建游标
        cursor = connection.cursor()
        url = 'https://baike.baidu.com/cms/home/eventsOnHistory/11.json?_=' + str(1699783815006)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
        }

        response = requests.get(url=url, headers=headers)

        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(response.json(), file, ensure_ascii=False)

        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        value = data["11"]
        value1 = value["1130"]
        for key in value1:
            name = jsonpath(key, '$..title')
            year = jsonpath(key, '$..year')
            desc = jsonpath(key, '$..desc')
            year = ''.join(year)
            print(year)

            for i in desc:
                s = re.sub('<.*?>', "", i)
            cg = (year, s)
            query = 'insert into student(year,thing) value (%s,%s)'
            cursor.execute(query, cg)
        connection.commit()
        connection.close()
    except pymysql.Error as e:
        print(str(e))
