import requests
from lxml import etree
import re
import json
import pymysql
pattern_num=r"\d+"
pattern_name=r"[\u4e00-\u9fa5]"
pattern_time=r"\d{4}-\d{2}-\d{2}"
if __name__=='__main__':
    db=pymysql.connect(host='localhost',user='root',password='666666',database='fzu_notice')
    cur=db.cursor()
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
            }
    url='https://jwch.fzu.edu.cn/jxtz.htm'
    page=0
    t_page=0
    while page<=1:#可自行控制页数
        page_text=requests.get(url=url,headers=headers).content
        tree=etree.HTML(page_text)
        if page ==0:
            t_page=int(tree.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/span[1]/span[9]//text()')[0])#总页数
        page+=1
        if page==1:
            url='https://jwch.fzu.edu.cn/'+tree.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/span[1]//*[@class="p_next p_fun"]/a/@href')[0]
        else:
            url='https://jwch.fzu.edu.cn/jxtz/'+tree.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/span[1]//*[@class="p_next p_fun"]/a/@href')[0]
        li_list=tree.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li')
        for li in li_list:
            detail_url='https://jwch.fzu.edu.cn/'+li.xpath('./a/@href')[0]#通知地址
            time=re.findall(pattern_time,''.join(li.xpath('./span/text()|./span/font/text()')))[0]#通知时间
            name=''.join(re.findall(pattern_name,li.xpath('./text()')[1]))#通知人
            title=li.xpath('./a/text()')[0]#通知的标题
            sql1="insert into notice (name,title,detail_url,time) values('%s','%s','%s','%s')"%(name,title,detail_url,time)
            cur.execute(sql1)
            #对detail_url访问提取附件
            detail_page_text=requests.get(url=detail_url,headers=headers).content
            detail_tree=etree.HTML(detail_page_text)
            ap_li=detail_tree.xpath('/html/body/div[1]/div[2]/div[2]/form/div/div[1]/div/ul/li')
            if len(ap_li)!=0:
                dap_li=ap_li[0]
                ap_name=dap_li.xpath('./a//text()')[0]
                ap_url='https://jwch.fzu.edu.cn'+dap_li.xpath('./a/@href')[0]#附件地址
                a = re.findall(pattern_num, dap_li.xpath('./span//text()')[0])
                u = 'https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid=' + a[0] + '&owner=' + a[1] + '&type=wbnewsfile&randomid=nattach'
                ui = json.loads(requests.get(url=u, headers=headers).text)#附件下载次数
                ap_num=int(ui['wbshowtimes'])#附件名字
    db.commit()
    db.close()
            #添加进数据库