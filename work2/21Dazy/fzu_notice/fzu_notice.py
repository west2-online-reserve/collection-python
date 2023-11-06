from lxml import etree
import requests
import re
import pymysql
def scrapy(input_url):#返回一页的html文本内容
    response=requests.get(url=input_url,headers=head,timeout=15)
    return response.content.decode('utf-8')
def paqu_fujian_nums(list_download):#利用ajax请求,参数为下载地址的url,返回一个二维列表，一个小列表包含一个附件的两个参数,返回值是附件的xi[url1,url2]
    list_result=[]#存放每个ajax请求的参数
    base_parram={'type':'wbnewsfile','randomid':'nattach','wbnewsid':0,'owner':0}
    list_download_nums=[]
    for base in list_download:
        parram_owner=re.match(pattern=pattern_parrams,string=base).group(1)
        parram_wbnewsid=re.match(pattern=pattern_parrams,string=base).group(2)
        base_parram['owner']=parram_owner
        base_parram['wbnewsid']=parram_wbnewsid
        list_result.append(base_parram)
        base_parram={'type':'wbnewsfile','randomid':'nattach','wbnewsid':0,'owner':0}
    for i in list_result:
        response=requests.get(headers=head,url=fujian_download_baseurl,params=i).json()
        list_download_nums.append(response['wbshowtimes'])
    return list_download_nums
def paqu_fujian(page_url):#爬取附件的下载地址，名称,下载次数
    content=scrapy(page_url)
    list_download=[]
    list_biaoti=[]
    result=[]
    if "附件【" in content:
        
        list_download=re.findall(pattern_fujian_download,content,re.S)
        list_biaoti=re.findall(pattern_fujian_name,content,re.S)
        list_nums=paqu_fujian_nums(list_download)
        n=len(list_biaoti)
        for i in range(n):
            result.append((notice_title,list_biaoti[i],list_download[i],list_nums[i]))
            
        return result
    else:
        
        return  0
if __name__=="__main__":
    notice_base_url="https://jwch.fzu.edu.cn"
    base_url="https://jwch.fzu.edu.cn/jxtz/"
    new_url='https://jwch.fzu.edu.cn/jxtz.htm'#最新的通知主页
    current_page=1
    fujian_download_baseurl='https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp'
    head={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    pattern_fujian_download=r'<li>附件.*?href="(/system/.*?download.jsp.*?wbfileid=\d{1,})"'#附件的下载地址
    pattern_fujian_name=r'<li>附件.*?href=.*?附件\d：(.*?)</a>'
    pattern_parrams=r'.*?owner=(\d+)&wbfileid=(\d+)'
    pattern_link=r'.*?(/info/\d+/\d+.htm).*?'
    
    page_xpath='/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/span[1]/span[9]/a/text()'
    detail_set_xpath='/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li'
    title_xpath='/html/body/div/div[2]/div[2]/form/div/div[1]/div/div[1]/h4//text()'
    writer_xpath='/html/body/div/div[2]/div[1]/p/a[3]/text()'
    time_xpath='/html/body/div/div[2]/div[2]/form/div/div[1]/div/div[2]/div[1]/span[1]/text()'
    
    response=requests.get(url=new_url,headers=head,timeout=15).content.decode('utf-8')
    response_html=etree.HTML(response)
    page_total=int(response_html.xpath(page_xpath)[0])
    
    db=pymysql.connect(host='localhost',user='root',password='yby258014',database='fzu_try')
    cur=db.cursor()
    sum=notice_num_need=int(input("你需要的消息数量\n"))#你需要的消息数
    create_table="create table fzu_notice(title text,time text,writer text,link text)"
    create_fujian="create table fzu_fujian(chuchu text,title text,downlink text,times int)"
    drop_table="drop table fzu_notice"
    drop_fujian="drop table fzu_fujian"
    try:
        cur.execute(create_table)
        cur.execute(create_fujian)
    except:
        print("该数据表已经存在,将为您更新至最新")
        cur.execute(drop_table)
        cur.execute(drop_fujian)
        cur.execute(create_table)
        cur.execute(create_fujian)
        while(notice_num_need>0):
                n=0
                page_notice_list=response_html.xpath(detail_set_xpath)#一个页面所有通知的html标签列表
                nums_page_notice=len(page_notice_list)#一个页面的通知数
                print("当前页面通知数",nums_page_notice)
                print('目前还需要爬取数量',notice_num_need)
                if len(page_notice_list)<=notice_num_need:
                    notice_num_need-=nums_page_notice
                    for one_notice in page_notice_list:#一次执行一次数据库插入
                        if re.match(r'.*?(info/\d+/\d+.htm).*?',one_notice.xpath("./a/@href")[0])  :
                            notice_link=notice_base_url+'/'+(re.match(r'.*?(info/\d+/\d+.htm).*?',one_notice.xpath("./a/@href")[0])).group(1)
                            notice_text=requests.get(url=notice_link,headers=head).content.decode('utf-8')
                            notice_html=etree.HTML(notice_text)
                            notice_writer=notice_html.xpath(writer_xpath)[0]
                            notice_title=one_notice.xpath("./a/@title")[0]
                            notice_time=notice_html.xpath(time_xpath)[0]
                            insert_execute_notice='''insert into fzu_notice(title,time,writer,link) values('%s','%s','%s','%s')'''%(notice_title,notice_time,notice_writer,notice_link)
                            insert_execute_fujian='''insert into fzu_fujian(chuchu,title,downlink,times) values("%s","%s","%s",%s)'''
                            cur.execute(insert_execute_notice) 
                            n+=1
                            if paqu_fujian(notice_link):
                                cur.executemany(insert_execute_fujian,paqu_fujian(notice_link))
                            db.commit()      
                else:
                    notice_num_need-=nums_page_notice
                    for one_notice in page_notice_list[0:notice_num_need]:#一次执行一次数据表插入
                        if re.match(r'.*?(info/\d+/\d+.htm).*?',one_notice.xpath("./a/@href")[0]):
                            notice_link=notice_base_url+'/'+re.match(r'.*?(info/\d+/\d+.htm).*?',one_notice.xpath("./a/@href")[0]).group(1)
                            notice_text=requests.get(url=notice_link,headers=head).content.decode('utf-8')
                            notice_html=etree.HTML(notice_text)
                            notice_writer=notice_html.xpath(writer_xpath)[0]
                            notice_title=one_notice.xpath("./a/@title")[0]
                            notice_time=notice_html.xpath(time_xpath)[0]
                            insert_execute_notice='''insert into fzu_notice(title,time,writer,link) values('%s','%s','%s','%s')'''%(notice_title,notice_time,notice_writer,notice_link)
                            insert_execute_fujian='''insert into fzu_fujian(chuchu,title,downlink,times) values("%s","%s","%s",%s)'''
                            cur.execute(insert_execute_notice)   
                            n+=1
                            if paqu_fujian(notice_link):
                                cur.executemany(insert_execute_fujian,paqu_fujian(notice_link))
                            db.commit()
                print("此轮插入数量"+str(n))
                page_total-=1
                page_url=base_url+str(page_total)+'.htm'
                response_page=requests.get(url=page_url,headers=head).content.decode('utf-8')
                response_html=etree.HTML(response_page)
        print("爬取结束")
        cur.close()
        db.close()
    else:
        print("正在为您收集数据")
        while(notice_num_need>0):
                page_notice_list=response_html.xpath(detail_set_xpath)#一个页面所有通知的html标签列表
                nums_page_notice=len(page_notice_list)#一个页面的通知数
                print(nums_page_notice)
                if len(page_notice_list)<=notice_num_need:
                    notice_num_need-=nums_page_notice
                    for one_notice in page_notice_list:#一次执行一次数据库插入
                        if re.match(r'.*?(info/\d+/\d+.htm).*?',one_notice.xpath("./a/@href")[0]):
                            notice_link=notice_base_url+'/'+re.match(r'.*?(info/\d+/\d+.htm).*?',one_notice.xpath("./a/@href")[0]).group(1)
                            notice_text=requests.get(url=notice_link,headers=head).content.decode('utf-8')
                            notice_html=etree.HTML(notice_text)
                            notice_writer=notice_html.xpath(writer_xpath)[0]
                            notice_title=one_notice.xpath("./a/@title")[0]
                            notice_time=notice_html.xpath(time_xpath)[0]
                            insert_execute_notice='''insert into fzu_notice(title,time,writer,link) values('%s','%s','%s','%s')'''%(notice_title,notice_time,notice_writer,notice_link)
                            insert_execute_fujian='''insert into fzu_fujian(chuchu,title,downlink,times) values("%s","%s","%s",%s)'''
                            cur.execute(insert_execute_notice)
                            if paqu_fujian(notice_link):
                                cur.executemany(insert_execute_fujian,paqu_fujian(notice_link))
                            db.commit()
                    
                else:
                    for one_notice in page_notice_list[0:notice_num_need]:#一次执行一次数据库插入
                        if re.match(r'.*?(info/\d+/\d+.htm).*?',one_notice.xpath("./a/@href")[0]):
                            notice_link=notice_base_url+'/'+re.match(r'.*?(info/\d+/\d+.htm).*?',one_notice.xpath("./a/@href")[0]).group(1)
                            notice_text=requests.get(url=notice_link,headers=head).content.decode('utf-8')
                            notice_html=etree.HTML(notice_text)
                            notice_writer=notice_html.xpath(writer_xpath)[0]
                            notice_title=one_notice.xpath("./a/@title")[0]
                            notice_time=notice_html.xpath(time_xpath)[0]
                            insert_execute_notice='''insert into fzu_notice(title,time,writer,link) values('%s','%s','%s','%s')'''%(notice_title,notice_time,notice_writer,notice_link)
                            insert_execute_fujian='''insert into fzu_fujian(chuchu,title,downlink,times) values("%s","%s","%s",%s)'''
                            cur.execute(insert_execute_notice)   
                            if paqu_fujian(notice_link):
                                cur.executemany(insert_execute_fujian,paqu_fujian(notice_link))
                            db.commit()
                page_total-=1
                page_url=base_url+str(page_total)+'.htm'
                response_page=requests.get(url=page_url,headers=head).content.decode('utf-8')
                response_html=etree.HTML(response_page)
        print("爬取结束")
        cur.close()
        db.close()
            
