import requests
from lxml import etree
import re
import json
import pymysql
pattern=r"[\u4e00-\u9fa5]"
pattern_2=r'\[.*?\]'
if __name__=='__main__':
    yea=[]
    db=pymysql.connect(host='localhost',user='root',password='666666',database='bdh')
    print('success')
    cur=db.cursor()
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
            }
    url='https://baike.baidu.com/cms/home/eventsOnHistory/0'+'%s'+'.json?_='
    num=1696082529004
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(6):
        page_text = requests.get((url+str(num-i))%(str(i+1))).json()
        if i+1>10:
            l1=str(i+1)
        else:
            l1='0'+str(i+1)
        for j in range(month[i]):
            if j+1<10:
                l2=l1+'0'+str(j+1)
                c=page_text[l1][l2]
            else:
                l2=l1+str(j+1)
                c=page_text[l1][l2]
            for d in c:
                year=d['year']
                title=''.join(re.findall(pattern,d['title']))
                type_=d['type']
                desct=d['desc']
                if len(desct)!=0:
                    tree=etree.HTML(desct)
                    de=re.sub(pattern_2,'',''.join(tree.xpath('//text()'))).replace("'",'')
                    print(len(de))
                    sql = "insert into bd (year,title,type,de) values('%s','%s','%s','%s')"%(year, title, type_, de)
                    cur.execute(sql)
                    db.commit()
                else:
                    sql = "insert into bd (year,title,type,de) values('%s','%s','%s','%s')" % (year, title, type_, '')
                    cur.execute(sql)
    #cur.execute("delete from bd")
    db.commit()
    db.close()

