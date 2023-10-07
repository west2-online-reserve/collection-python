'''要求:

获取一年内每天的历史上的今天发生了什么，包括年份，事件类型(birth、death等)，标题，简要内容
上述内容一律要去除回车、括号等无用符号
把爬取到的数据存入数据库中'''
import requests,re,pymysql
from lxml import etree
day=''#-----日期
year=[]
thing=[]
url='https://www.lssjt.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"}
def handle(i):
    pattern = r'[《》/:?"。\\，*：（）【】]'
    i = re.sub(pattern, '', i)
    return i
def response():
    global day
    today=requests.get(url=url,headers=headers).text
    tday=etree.HTML(today).xpath('/html/body/div[4]/div[1]/h1/text()')[1]
    day=re.findall('的(.*?)今',tday)[0]
    things = etree.HTML(today).xpath('//*[@id="container"]/li')[1:-1]
    for i in things:
        n=i.xpath('.//text()')
        date=n[2]
        thingday=n[11]+n[13]
        year.append(date)
        thing.append(handle(thingday))
response()
def pmysql():#----建表
    mysql=pymysql.connect(host='127.0.0.1',user='root',password='123456',port=3306)
    cursor=mysql.cursor()
    cursor.execute('show databases;')
    res=cursor.fetchall()
    #print(res)
    if  re.findall('db',str(res))!=[]:
        cursor.execute('use db;')
    else:
        cursor.execute('create database db;')
        cursor.execute('use db;')
    cursor.execute('show tables')
    res=cursor.fetchall()
    #print(res)
    #cursor.execute('create table Todaything(id int not null auto_increment primary key,日期 varchar(32) not null,事件 varchar(256) not null)default charset=utf8;')
    mysql.close()
pmysql()
def writesql():
    mysql=pymysql.connect(host='127.0.0.1',user='root',password='123456',port=3306)
    cursor=mysql.cursor()
    cursor.execute('use db;')
    #insert into 表名（列名, 列名, 列名) values(对应列的值, 对应列的值, 对应列的值);
    k=0
    #print(year)
    for i in year:
        k+=1
        a=f'insert into Todaything(id,日期,事件) value(%s,%s,%s)'
        print(k,i,thing[k-1])
        cursor.execute(a,(k,i,thing[k-1]))
        mysql.commit()
    cursor.close()
    mysql.close()
writesql()
