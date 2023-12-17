import re
from bs4 import BeautifulSoup
import requests
import pymysql
def find_file(url,author):
    file_list = []
    try:
        res = requests.get(url)
        res.encoding = 'utf-8'
        if re.search(r'附件【', res.text):
            soup = BeautifulSoup(res.text, 'lxml').find(name='ul', attrs={'style': 'list-style-type:none;'})
            for li in soup.find_all(name='li'):
                name = li.a.string
                num = li.span.string
                download_url="https://jwch.fzu.edu.cn" + li.a['href']
                wbnewsid = re.search(r'getClickTimes\((\d*?),', num).group(1)
                url = f'https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid={wbnewsid}&owner=1744984858&type=wbnewsfile&randomid=nattach'
                num = requests.get(url).json().get('wbshowtimes')
                file_list.append({"name": name, "download_num": num,"download_url":download_url,'author':author})
        return file_list
    except(requests.exceptions.ConnectionError):
        return file_list
def page_number(url):
    res=requests.get(url)
    res.encoding='utf-8'
    num=re.search(r'<a href="jxtz/1.htm">(\d{3})</a>',res.text,re.S).group(1)
    return num
def find_time(soup):
    time_list = []
    for li in soup.find('div',class_='box-gl clearfix').find_all('li'):
        str1=li.span.text
        str2=str1.replace('\n', '').replace('\r', '').replace(' ','')
        time_list.append(str2)
    return time_list
def find_author(soup):
    author_list = []
    for li in soup.find('div', class_='box-gl clearfix').find_all('li'):
        author_list.append(re.search(r'【(.*?)】',str(li)).group(1))
    return author_list
def find_title(soup):
    title_list = []
    for li in soup.find('div', class_='box-gl clearfix').find_all('li'):
        title_list.append(li.a['title'])
    return title_list
def find_url(soup):
    notice_url_list = []
    for li in soup.find('div', class_='box-gl clearfix').find_all('li'):
        if li.a['href'][0] == '.':
            info_link = "https://jwch.fzu.edu.cn" + li.a['href'][2:]
        elif li.a['href'][0] == 'i':
            info_link = "https://jwch.fzu.edu.cn" + li.a['href']
        else:
            info_link = li.a['href']
        notice_url_list.append(info_link)
    return notice_url_list
if __name__ == '__main__':
    author_list=[]
    title_list=[]
    time_list=[]
    notice_url_list=[]
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
    fzu_url = 'https://jwch.fzu.edu.cn/jxtz.htm'
    url_list = []
    url_list.append(fzu_url)
    all_page=int(page_number(fzu_url))
    print("总页数为：",all_page)
    for i in range(1, 5):
        next_url = f"https://jwch.fzu.edu.cn/jxtz/{all_page - i}.htm"
        url_list.append(next_url)
    for url in url_list:
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'lxml')
        time_list=time_list+find_time(soup)
        author_list=author_list+find_author(soup)
        title_list=title_list+find_title(soup)
        notice_url_list=notice_url_list+find_url(soup)
    db=pymysql.connect(host="127.0.0.1", user="root", password="123456", database="fzu_notice", charset='utf8')
    cur=db.cursor()
    insert_sql="""INSERT INTO NOTICE(AUTHOR,TITLE,TIME,URL) VALUES(%s,%s,%s,%s);"""
    for i in range(0,100):
        cur.execute(insert_sql,(author_list[i],title_list[i],time_list[i],notice_url_list[i]))
    db.commit()
    files_list=[]
    for i in range(0,100):
        files_list += find_file(notice_url_list[i],author_list[i])
    insert_sql = """INSERT INTO FILES(NAME,DOWNLOAD_NUM,DOWNLOAD_URL,AUTHOR) VALUES(%s,%s,%s,%s);"""
    for li in files_list:
        cur.execute(insert_sql, (li['name'],li['download_num'],li['download_url'],li['author']))
    db.commit()
