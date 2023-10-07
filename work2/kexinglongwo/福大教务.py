'''爬取福大教务通知 https://jwch.fzu.edu.cn/jxtz.htm

要求:

获取教务通知(最近100条即可，但需要获取总页数或条数)
提取通知信息中的“通知人”(如：质量办、计划科)、标题、日期、详情链接。
爬取通知详情的html，可能存在“附件”，提取附件名，附件下载次数，附件链接吗，有能力请尽可能将附件爬取下来。
上述内容一律要去除回车、括号等无用符号
把除附件外爬取到的数据存入数据库中'''
import requests,pymysql,re
from lxml import etree
url='https://jwch.fzu.edu.cn/jxtz.htm'
urlm='https://jwch.fzu.edu.cn/jxtz/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"}
a = requests.get(url=url, headers=headers)
a.encoding = 'utf-8'
a = a.text
Notice=[]    #---通知人
time=[]      #---通知时间
title=[]     #----通知名称
urlall=[]    #----url
frequency={} #--- -附件    {'名称':{附件名：次数}}
def extract_parameters(string):
    pattern = r'getClickTimes\((\d+),(\d+),"([^"]+)","([^"]+)"\)'
    matches = re.search(pattern, string)
    if matches:
        param1 = int(matches.group(1))
        param2 = int(matches.group(2))
        param3 = matches.group(3)
        param4 = matches.group(4)
        if param3==None:
            param3='wbnews'
        if param4!=None:
            param4='n'+param4

        return param1, param2, param3, param4
    else:
        return None
def handle(i):
    i=i.replace('《','')
    i = i.replace('》', '')
    i=i.replace("/", "")
    i = i.replace(":", "")
    i = i.replace("?", "")
    i = i.replace('"', "")
    i = i.replace("。", "")
    i = i.replace("\\", "")
    i = i.replace("，", "")
    i = i.replace("*", "")
    i = i.replace("：", "")
    i = i.replace("（", "")
    i = i.replace("）", "")
    i = i.replace("【", "")
    i = i.replace("】", "")
    return i
def find(disc:list):                                                        #----找到通知人、标题、日期、详情链接
    b=[]
    for i in disc:
        if i.strip() ==None or i.strip()=='':
            continue
        else:
            b.append(i.strip())
    return b
def max_page():                                                      #找到最大页
    b=etree.HTML(a).xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/span[1]/span//text()')
    c=None
    for i in b:
        if str(i).isdigit():
            dig =int(i)
            if c is None or dig>c:
                c=dig
    return c
def notice(aurl=url):                           #--------------------------------
    a = requests.get(url=aurl, headers=headers)
    a.encoding='utf-8'
    Notifyperson=etree.HTML(a.text).xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li')
    for i in Notifyperson:
        desc=i.xpath('.//text()')#海豹符
        c= find(desc)
        #print(c:=find(desc))
        time.append(c[0])
        Notice.append(handle(c[1]))
        title.append(handle(c[2]))
        b=i.xpath('./a/@href')[0]
        #https: // jwch.fzu.edu.cn / info / 1040 / 12864.htm
        #print(b)
        ll=re.findall('info/(.*?).htm',b)[0]
        #print(ll)
        urlall.append('https://jwch.fzu.edu.cn/info/'+ll+'.htm')
        #print('https://jwch.fzu.edu.cn/info/'+ll+'htm')
def notice100():#-----100条
    t=max_page()
    i=1
    o=True
    while o:
        if i<=1:
            i+=1
            notice(url)
        elif 1<=i<=5:
            i+=1
            notice(urlm+f'{t-i}.htm')
        else:
            o=False
notice100()
def attachment():
    for e in range(100):
        contont = {}  # ----{附件 }
        a=requests.get(url=urlall[e],headers=headers)
        a.encoding = 'utf-8'
        b=etree.HTML(a.text).xpath('.//ul[@style="list-style-type:none;"]/li')
        #print(b)
        for i in b:
            d=i.xpath('.//text()')[1]
            #print(d)
            k=i.xpath('.//@href')[0]
            c=i.xpath('./span//text()')[0]
            x,y,z,n=extract_parameters(c)
            t=requests.get(f'https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid={x}&owner={y}&type={z}&randomid={n}',headers=headers).text
            #print(t)
            t=re.findall('"wbshowtimes":(.*?),"rand',t)[0]
            contont[d]='https://jwch.fzu.edu.cn'+k+'下载'+t+'次'
            #print(t)
            #print(contont)
        frequency[title[e]]=contont
attachment()
#print(title)
#print(frequency)
#------------------------------------------------pymysql
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
    cursor.execute('create table Notice(id int not null auto_increment primary key,通知人 varchar(32) not null,标题 varchar(64) not null,日期 varchar(64) not null,详情链接 varchar(64) not null,附件信息 text not null)default charset=utf8;')
    mysql.close()
pmysql()
def writesql():
    mysql=pymysql.connect(host='127.0.0.1',user='root',password='123456',port=3306)
    cursor=mysql.cursor()
    cursor.execute('use db;')
    #insert into 表名（列名, 列名, 列名) values(对应列的值, 对应列的值, 对应列的值);
    for i in range(100):
        id = i + 1
        n = Notice[i]
        t=title[i]
        ti=time[i]
        ur=urlall[i]
        fr=str(frequency[title[i]])
        a=(f'insert into Notice(id,通知人,标题,日期,详情链接,附件信息) values(%s,%s,%s,%s,%s,%s)')
        #a=f'insert into Notice(id,通知人,标题,日期,详情链接,附件信息) values({i+1},{Notice[i]},{title[i]},{time[i]},{urlall[i]},%s)'
        #cursor.execute(a)
        try:
            # 执行SQL语句
            cursor.execute(a, (id, n,t,ti,ur,fr))
            # 提交事务
            mysql.commit()
            print("插入成功")
        except Exception as e:
            # 发生错误时回滚
            mysql.rollback()
            print("插入失败：" + str(e))
    cursor.close()
writesql()
#print(urlall)