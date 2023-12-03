import re
import pymysql
import requests
from lxml import etree

pages = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'}
url = "https://jwch.fzu.edu.cn/jxtz.htm"
conn = pymysql.connect(host='localhost', user='root', password='3d1415926', database='mydb')
cursor = conn.cursor()

page_1 = requests.get(url=url, headers=headers).content
pages.append(page_1)
page_list = etree.HTML(page_1).xpath('//span[@class="p_no"]')
for i in page_list[:-1]:
    pages.append(requests.get(url='https://jwch.fzu.edu.cn/' + i.xpath('./a/@href')[0], headers=headers).text)
print(f'共{page_list[-1].xpath("./a/text")[0]}页!\n')

for i in pages:
    content_list = etree.HTML(i).xpath('.//ul[@class="list-gl"]/li')
    for j in content_list:
        url = 'https://jwch.fzu.edu.cn/' + j.xpath('./a/@href')[0]
        content = requests.get(url=url, headers=headers).content
        notifer = etree.HTML(content).xpath('//p[@class="w-main-dh-text"]/a[3]/text()')[0]
        title = etree.HTML(content).xpath('//div[@class="xl_tit"]/h4/text()')[0]
        time = etree.HTML(content).xpath('//span[@class="xl_sj_icon"]/text()')[0][5:]
        annex = etree.HTML(content).xpath('//ul[@style="list-style-type:none;"]/li')
        if annex:
            for k in range(len(annex)):
                annex_url = 'https://jwch.fzu.edu.cn' + annex[k].xpath('./a/@href')[0]
                annex_name = annex[k].xpath('./a//text()')[0]
                annex_number = annex[k].xpath('./span//text()')[0]
                num = re.findall('\d+', annex_number)
                data = {'wbnewsid': num[0], 'owner': num[1], 'type': 'wbnewsfile', 'randomid': 'nattach'}
                num_url = 'https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp'
                content = requests.post(num_url, data=data, headers=headers)
                annex_number = content.json()['wbshowtimes']
                sql = """INSERT INTO FZUDB(URL,NOTIFER,TITLE,TIME,ANNEX_URL,ANNEX_NAME,ANNEX_NUMBER)
                         VALUES ('%s','%s','%s','%s','%s','%s','%d')"""%(url,notifer,title,time,annex_url,annex_name,annex_number)
                cursor.execute(sql)
        else:
            sql = """INSERT INTO FZUDB(URL,NOTIFER,TITLE,TIME)
                     VALUES ('%s','%s','%s','%s')"""%(url,notifer,title,time)
            cursor.execute(sql)

conn.commit()
cursor.close()
conn.close()
