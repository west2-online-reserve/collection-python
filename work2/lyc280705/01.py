import requests
import re
import pymysql
from lxml import etree
from urllib.parse import urljoin
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='fzu_notice')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS notice;")
create_table_sql = """
    CREATE TABLE notice (
        id INT(11) NOT NULL AUTO_INCREMENT,
        page_text TEXT,
        time VARCHAR(50),
        title VARCHAR(255),
        section VARCHAR(255),
        info_url VARCHAR(255),
        attach_url VARCHAR(255),
        attach_name TEXT,
        attach_times INT(11),
        PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""
cursor.execute(create_table_sql)
start_url = "https://jwch.fzu.edu.cn"
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31'
}
page=1
parser = etree.HTMLParser(encoding="utf-8")
next_url = ""
while page<=5:
        if page==1:
            page_text = requests.get(url=start_url+'/jxtz.htm', headers=headers).text.encode(encoding="ISO-8859-1")
            tree = etree.HTML(page_text, parser=parser)
            next_url = tree.xpath('//span[@class="p_next p_fun"]/a/@href')[0]
            li_list=tree.xpath('//ul[@class="list-gl"]/li')
            for li in li_list:
                time=li.xpath('./span//text()')[0]
                title=li.xpath('./a/text()')[0]
                section=li.xpath('./text()')[1]
                info_url='https://jwch.fzu.edu.cn/'+li.xpath('./a/@href')[0]
                print(time,title,section,info_url,page)
                detail_page_text=requests.get(url=info_url,headers=headers).text.encode(encoding="ISO-8859-1")
                detail_tree=etree.HTML(detail_page_text,parser=parser)
                attach_url=""
                attach_name=""
                attach_times=""
                if detail_tree.xpath('//div[@class="xl_main"]/ul/li/a/@href'):
                    attach_url=start_url+detail_tree.xpath('//div[@class="xl_main"]/ul/li/a/@href')[0]
                    attach_name=detail_tree.xpath('//div[@class="xl_main"]/ul/li/a/text()')
                    wbnewsid=detail_tree.xpath('//div[@class="xl_main"]/ul/li/span/@id')
                    owner=detail_tree.xpath('/html/head/script[5]')
                    attach_url_get=requests.get(url='https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid='+ re.findall(r'\d+', wbnewsid[0])[0]+ '&owner='+re.findall(r'\d+', owner[0].text)[2]+'&type=wbnewsfile&randomid=nattach', headers=headers).text
                    attach_times=re.findall(r'\d+', attach_url_get)[0]
                    print(attach_url,attach_name,attach_times)
                    sql1 ="INSERT INTO notice (page_text, time, title, section, info_url,attach_url, attach_name, attach_times) VALUES (%s, %s, %s,%s,%s, %s, %s, %s)"
                    cursor.execute(sql1,(page_text,str(time), str(title), str(section), str(info_url),str(attach_url), str(attach_name), attach_times))
                    db.commit()
                else:
                    sql2 ="INSERT INTO notice (page_text, time, title, section, info_url) VALUES (%s,%s, %s, %s, %s)"
                    cursor.execute(sql2,(page_text,str(time), str(title), str(section), str(info_url)))
                    db.commit()
            page+=1
        elif page==2:
            page_text = requests.get(url=start_url+'/'+next_url, headers=headers).text.encode(encoding="ISO-8859-1")
            tree = etree.HTML(page_text, parser=parser)
            next_url = tree.xpath('//span[@class="p_next p_fun"]/a/@href')[0]
            li_list=tree.xpath('//ul[@class="list-gl"]/li')
            for li in li_list:
                time=li.xpath('./span//text()')[0]
                title=li.xpath('./a/text()')[0]
                section=li.xpath('./text()')[1]
                info_url=[urljoin('https://jwch.fzu.edu.cn',li.xpath('./a/@href')[0])][0]
                print(time,title,section,info_url,page)
                detail_page_text=requests.get(url=info_url,headers=headers).text.encode(encoding="ISO-8859-1")
                detail_tree=etree.HTML(detail_page_text,parser=parser)
                if detail_tree.xpath('//div[@class="xl_main"]/ul/li/a/@href'):
                    attach_url=start_url+detail_tree.xpath('//div[@class="xl_main"]/ul/li/a/@href')[0]
                    attach_name=detail_tree.xpath('//div[@class="xl_main"]/ul/li/a/text()')
                    wbnewsid=detail_tree.xpath('//div[@class="xl_main"]/ul/li/span/@id')
                    owner=detail_tree.xpath('/html/head/script[5]')
                    attach_url_get=requests.get(url='https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid='+ re.findall(r'\d+', wbnewsid[0])[0]+ '&owner='+re.findall(r'\d+', owner[0].text)[2]+'&type=wbnewsfile&randomid=nattach', headers=headers).text
                    attach_times=re.findall(r'\d+', attach_url_get)[0]
                    print(attach_url,attach_name,attach_times)
                    sql1 ="INSERT INTO notice (page_text, time, title, section, info_url,attach_url, attach_name, attach_times) VALUES (%s, %s, %s,%s,%s, %s, %s, %s)"
                    cursor.execute(sql1,(page_text,str(time), str(title), str(section), str(info_url),str(attach_url), str(attach_name), attach_times))
                    db.commit()
                else:
                    sql2 ="INSERT INTO notice (page_text, time, title, section, info_url) VALUES (%s,%s, %s, %s, %s)"
                    cursor.execute(sql2,(page_text,str(time), str(title), str(section), str(info_url)))
                    db.commit()
            page+=1
        else:
            page_text = requests.get(url=start_url+'/jxtz/'+next_url, headers=headers).text.encode(encoding="ISO-8859-1")
            tree = etree.HTML(page_text, parser=parser)
            next_url = tree.xpath('//span[@class="p_next p_fun"]/a/@href')[0]
            li_list=tree.xpath('//ul[@class="list-gl"]/li')
            for li in li_list:
                time=li.xpath('./span//text()')[0]
                title=li.xpath('./a/text()')[0]
                section=li.xpath('./text()')[1]
                info_url=[urljoin('https://jwch.fzu.edu.cn',li.xpath('./a/@href')[0])][0]
                print(time,title,section,info_url,page)
                detail_page_text=requests.get(url=info_url,headers=headers).content.decode('utf-8')
                detail_tree=etree.HTML(detail_page_text,parser=parser)
                if detail_tree.xpath('//div[@class="xl_main"]/ul/li/a/@href'):
                    attach_url=start_url+detail_tree.xpath('//div[@class="xl_main"]/ul/li/a/@href')[0]
                    attach_name=detail_tree.xpath('//div[@class="xl_main"]/ul/li/a/text()')
                    wbnewsid=detail_tree.xpath('//div[@class="xl_main"]/ul/li/span/@id')
                    owner=detail_tree.xpath('/html/head/script[5]')
                    attach_url_get=requests.get(url='https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid='+ re.findall(r'\d+', wbnewsid[0])[0]+ '&owner='+re.findall(r'\d+', owner[0].text)[2]+'&type=wbnewsfile&randomid=nattach', headers=headers).text
                    attach_times=re.findall(r'\d+', attach_url_get)[0]
                    print(attach_url,attach_name,attach_times)
                    sql1 ="INSERT INTO notice (page_text, time, title, section, info_url,attach_url, attach_name, attach_times) VALUES (%s, %s, %s,%s,%s, %s, %s, %s)"
                    cursor.execute(sql1,(page_text,str(time), str(title), str(section), str(info_url),str(attach_url), str(attach_name), attach_times))
                    db.commit()
                else:
                    sql2 ="INSERT INTO notice (page_text, time, title, section, info_url) VALUES (%s,%s, %s, %s, %s)"
                    cursor.execute(sql2,(page_text,str(time), str(title), str(section), str(info_url)))
                    db.commit()
            page+=1
db.close()