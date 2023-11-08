import json
import requests
import pymysql
import re

conn = pymysql.connect(host = 'localhost',port=3306,user='root',password ='040426',database = 'spider',charset='utf8mb4')
cursor = conn.cursor()

def write_to_db(data):
    cursor.executemany(
        'insert into `baidu_calenaer` (`year`,`type`,`title`,`desc`) values(%s,%s,%s,%s)',data
    )
    conn.commit()
    data.clear()

def match(text):
    pattern = re.compile(r'<[^<>]+>|([^<>]+)')
    matches = ''.join(re.findall(pattern, text))
    matches = re.sub(r'\n', '', matches)
    return matches

months_lst = ['01','02','03','04','05','06','07','08','09','10','11','12']
days_lst = [31,29,31,30,31,30,31,31,30,31,30,31]

headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
}
datas_lst = []
for month in months_lst:
    url = f"https://baike.baidu.com/cms/home/eventsOnHistory/{month}.json?_=1696935144306"
    response = requests.get(url=url,headers=headers).text
    web_data_dic = (json.loads(response))[str(month)]
    days_num_lst = [i for i in web_data_dic.keys()]
    days_num_lst = days_num_lst[::-1]
    for day in days_num_lst:                #day包含月+日，如0131为1月31日
        for a_day_lst in web_data_dic[day]:#a_day_lst为一个日期下众多事件的 列表 ，列表中内容为字典
            web_today = a_day_lst
            title = match(web_today['title'])
            year = web_today['year']+','+day
            type = web_today['type']
            desc = match(web_today['desc'])
            datas_lst.append((year,type,title,desc))
        write_to_db(datas_lst)
        print(day,'日，已完成')
    print(month+'月,已完成\n--------------------------------------------')
conn.close()


