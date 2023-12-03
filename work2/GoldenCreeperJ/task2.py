import re
import pymysql
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'}
data = {'_': 0}
url = 'https://baike.baidu.com/cms/home/eventsOnHistory/'
mouth_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
conn = pymysql.connect(host='localhost', user='root', password='3d1415926', database='mydb')
cursor = conn.cursor()

for i in range(12):
    content = requests.get(url=url + f'{i+1:02}.json?', data=data, headers=headers).json()
    for j in range(mouth_day[i]):
        history = content[f'{i + 1:02}'][f'{(i + 1) * 100 + j + 1:04}']
        for k in history:
            type = k['type']
            year = k['year'].strip()
            title = re.sub('<.+?>', '', k['title'])
            desc = re.sub('<.+?>', '', k['desc']) + '...'
            desc = re.sub('\'','\\\'',desc)
            if year>'0':
                sql = '''INSERT INTO TODAY(YEAR,TITLE,TYPE,`DESC`)
                         VALUES ('%s','%s','%s','%s');''' % (year + f'-{i + 1:02}-{j + 1:02}', title, type, desc)
                cursor.execute(sql)

conn.commit()
cursor.close()
conn.close()
