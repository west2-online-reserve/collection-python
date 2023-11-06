import requests
import pymysql
import re 
from lxml import etree
import datetime
import json
def today():#如果要特定某一天的话可以用上
    current_date=datetime.date.today()
    s_current=str(current_date)
    l_date=s_current.split('-')
    return l_date


def scarpy(url):
    html_text=requests.get(headers=head,url=url)
    return html_text.content.decode('utf-8')
def scarpy_html(url):
    html_text=scarpy(url)
    html=etree.HTML(html_text)
    return html
#def analysis_json先留着，看看能不能再把整个json的解析函数化
    
def scarpy_text(event_html):
    tree_desc=etree.HTML(event_html)#把html语言的文本转化为html标签，以供使用xpath，来获取所有text内容
    if tree_desc==None:
        return "空"
    desc_text_list=tree_desc.xpath("//text()")#返回了一个包含所有text的列表，把列表
    str_text ="".join(desc_text_list)
    str_text=str_text.replace("'","''")
    return str_text

    


def main_scarpy():#获取当当年每一天历史发生的重要事件,及其年份，类型，概述，
    
    for mon in range(1,13):#月份的遍历
        if mon<10:
            month='0'+str(mon)
        month_ajax_url='https://baike.baidu.com/cms/home/eventsOnHistory/%s.json'%(month)
        response=requests.get(headers=head,url=month_ajax_url)
        month_json=response.json()
        month=list(month_json.keys())[0]#这个月月份
        days_dict=month_json[month]#一个字典包含每天对应的历史事件 ，拿12月为例，‘首个’键值对是这样'1231':[... ],注意这个字典是倒序，第一个键值对是当月最后一天
        days=len(days_dict)#这个月天数
        for day in range(1,days+1):#日数的遍历
            if day<10:
                key_day='0'+str(day)
                key_day=month+key_day
            the_day_lievent=days_dict[key_day]#存放当天所有历史事件信息的列表，每一个元素为一个字典
            for single_event in the_day_lievent:#提取每一个单独事件，一个事件以字典形式存放,['#year', '#title', '#festival', 'link', '#type', '#desc', 'cover', 'recommend']这是一个事件字典所有键的名称，需要提取的这里打＃,每读完一次事件存储一次
                event_year=str(single_event['year'])#事件年份
                event_title=scarpy_text(single_event['title'])#事件标题，由于是html形式所以这边使用这个函数
                event_type=str(single_event['type'])#事件类型
                event_desc=scarpy_text(single_event['desc'])#事件概要
                event_link=single_event['link']#因为desc不全，存放详情页面的link
                execute_insert_true="insert into history(year_event,title_event,type_event,desc_event,link_event) values('%s','%s','%s','%s','%s')"%(event_year,event_title,event_type,event_desc,event_link)
                cur.execute(execute_insert_true)
                db.commit()
                
pattern=re.compile('')

baseurl_ajax='https://baike.baidu.com/cms/home/eventsOnHistory/{}.json'
head={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
pattern=re.compile('(\d+)')
total_data_xpath='/html/body/div[2]/div/div[2]/div/div/dl/dd'
desc_xpath='/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/text'
l_today=today()
if __name__=="__main__":
    
    table_name="history"
    db=pymysql.connect(host='localhost',password='yby258014',user='root',database='today_in_history')
    cur=db.cursor()
    
    
    execute_create_table="create table history(year_event text,title_event text,type_event text,desc_event text,link_event text)"
    #cur.execute(execute_create_table)
    try:
        cur.execute(execute_create_table)
    except:
        execute_drop="drop table history"
        cur.execute(execute_drop)
        print("该数据表已存在，故为您更新至最新")
        cur.execute(execute_create_table)
        main_scarpy()
        cur.close()
        db.close()
        
    else:
        main_scarpy()            
        cur.close()
        db.close()
     
        
    
