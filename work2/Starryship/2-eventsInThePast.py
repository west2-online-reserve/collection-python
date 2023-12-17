'''爬取百度百科历史上的今天 https://baike.baidu.com/calendar/

要求:

获取一年内每天的历史上的今天发生了什么，包括年份，事件类型(birth、death等)，标题，简要内容
上述内容一律要去除回车、括号等无用符号
把爬取到的数据存入数据库中'''

import requests
from bs4 import  BeautifulSoup
from pymysql import connect


#建表
def tab(day):

    sql='''

    create table %s(

    id int not null auto_increment primary key,
    year int,
    type varchar(128),
    title varchar(128),
    brief_content varchar(512)

    )

    '''%day
    cursor.execute(sql)
    con.commit()

#住函数，实现数据的爬取和数据的读入操作
def main():
    for i in range(1, 13):
        day=0
        n = str(1699192092181 - i)

        if i < 10:
            st = "0" + str(i)
        else:
            st = str(i)

        url = "https://baike.baidu.com/cms/home/eventsOnHistory/%s.json?_=%s" % (st, n)

        response = requests.get(url=url, headers=headers).json()

        li = response[st].keys()
        for l in reversed(li):
            a = response[st][l]
            day += 1
            date = str(i) + "月" + str(day) + "日"
            tab(date)
            for b in a:
                #类型
                ty=b["type"]
                #年份
                ye=b["year"]
                # 标题
                ti = BeautifulSoup(b["title"], "lxml").text.strip()
                # 简要内容
                te=BeautifulSoup(b["desc"],"lxml").text.replace("'","")

                sql2="insert into %s (year,type,title,brief_content) values('%s','%s','%s','%s')" % (date,ye,ty,ti,te)
                cursor.execute(sql2)
                con.commit()


if __name__=="__main__":

    # 连接数据库
    con = connect(host='127.0.0.1', port=3306, user='root', password='root', charset='utf8')
    # 创建游标
    cursor = con.cursor()
    # 创建数据库
    cursor.execute("create database if not exists xing DEFAULT CHARSET utf8 COLLATE utf8_general_ci")
    # 使用数据库
    cursor.execute("use xing")

    headers = {"User-Agent":
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}

    #调用主函数
    main()

    cursor.close()
    con.close()






