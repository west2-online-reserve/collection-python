import requests
import re
import pymysql
basic_url="https://baike.baidu.com/cms/home/eventsOnHistory/"
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31'
}
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='history')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS history;")
create_table_sql = """
    CREATE TABLE history (
        id INT(11) NOT NULL AUTO_INCREMENT,
        year VARCHAR(50),
        title_text VARCHAR(255),
        _type VARCHAR(255),
        desc_text TEXT,
        PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""
cursor.execute(create_table_sql)
for i in range(1,13):
    month_str='{:02d}'.format(i)
    url=basic_url+month_str+".json?_=16970370778"+str(95-i)
    response = requests.get(url=url, headers=headers)
    data=response.json()
    for month in data.values():
        for day in month.values():
                for event in day:
                        if 'year' in event:
                                desc = event['desc']
                                title = event['title']
                                year = event['year']
                                _type=event['type']
                                print(event['year'],event['type'])
                                desc_text = re.sub('<.*?>', '', desc)
                                title_text = re.sub('<.*?>', '', title)
                                print(title_text,desc_text)
                                sql1 ="INSERT INTO history (year,_type, title_text, desc_text) VALUES (%s, %s, %s,%s)"
                                cursor.execute(sql1,(str(year), str(_type), str(title_text), str(desc_text)))
                                db.commit()
db.close()