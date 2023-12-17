import pymysql
import requests
import re
def delect_str(content_str):
    str_list = re.findall(r'(<.*?>)', content_str)
    for str in str_list:
        content_str = content_str.replace(str, '')
    return content_str
if __name__=='__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    everyday_list=[]
    for i in range(0,12):
        if(i<9):
            str_='0'+str(i+1)
        else:
            str_=str(i+1)
        year_url=f'https://baike.baidu.com/cms/home/eventsOnHistory/'+str_+'.json'
        res = requests.get(url=year_url, headers=headers)
        res.encoding = 'utf-8'
        res_text = res.json()
        for day in range(1,month[i]+1):
            if day<10:
                day_str=str_+'0'+str(day)
            else:
                day_str=str_+str(day)
            #year_list.append(res_text[str_][day_str])
            for li in res_text[str_][day_str]:
                title_str=delect_str(li['title'])
                content_str=delect_str(li['desc'])
                today_dict={'year':li['year'],'type':li['type'],'title':title_str,'content':content_str}
                everyday_list.append( today_dict)
    db = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="baidu", charset='utf8')
    cur = db.cursor()
    insert_sql = """INSERT INTO EVENTS(YEAR,TYPE,TITLE,CONTENT) VALUES(%s,%s,%s,%s);"""
    for dic in everyday_list:
        cur.execute(insert_sql,(dic['year'],dic['type'],dic['title'],dic['content']))
    db.commit()