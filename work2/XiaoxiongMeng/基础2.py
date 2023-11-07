import sys
import requests
import pymysql
import re
import time

TT = 0
print('请先登录数据库!')
suser = input('请输入MySQL的用户名user:')
spassword = input('请输入MySQL用户"' + suser + '"的密码:')
db = pymysql.connect(host='localhost',user=suser,password=spassword,database='PYTHON')
c = db.cursor()
c.execute("TRUNCATE TABLE python.historytoday;")
db.commit()
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
for i in month:
    postUrl = 'https://baike.baidu.com/cms/home/eventsOnHistory/' + i + '.json?_=1668083268575'
    xx = requests.get(postUrl, headers=ua)
    xx.encoding = 'utf-8'
    t = xx.json()
    for u in range(1, days[int(i) - 1] + 1):
        TT += 1
        date = ''
        if u < 10:
            date = i + '0' + str(u)
        else:
            date = i + str(u)
        todayHistory = t[i][date]
        no = 0
        for m in todayHistory:
            no += 1
            m['title'] = re.sub("<(.|\n)*?>", '', m['title'])
            m['desc'] = re.sub("<(.|\n)*?>", '', m['desc'])
            m['title'] = m['title'].replace("'","`")
            m['desc'] = m['desc'].replace("'", "`")
            m['desc'] = m['desc'] + '...'
            m['desc'] = re.sub("<(.|\n)*?\.", '', m['desc'])
            if m['type'] == 'birth':
                typet = '神人诞生\n'
            elif m['type'] == 'death':
                typet = '巨星陨落\n'
            else:
                typet = '其他类型\n'
            c.execute(
                "insert into python.historytoday (year,date,title,number,content,detail,type) values('"+m['year']+"','" + date + "','" + m['title'
                ] + "','" + str(no) + "','" + m['desc'] + "','" + m['link'] + "','"+typet+"');")
            db.commit()
            print("\r", end="")
            print("存储到数据库进度: {}% ".format(int((TT )/ 366 * 100)),"▓" * int(((TT / 366) * 100) // 2), end="")
            sys.stdout.flush()
db.close()
c.close()
print("\n数据已保存至数据库.")
