import json
import os

import mysql.connector
import requests
from bs4 import BeautifulSoup

# 创建文件夹
folder_path = 'attachments_folder'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}


def crawl(url, cursor):
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')

    li_list = soup.select('div[class="box-gl clearfix"] > ul > li')
    for li in li_list:
        date = li.find('span').text.strip()
        title = li.find('a').text.strip()
        details_url = li.find('a')['href']
        # 去除span和a中的内容以保证获取的只有通知人
        for span in li.find_all('span'):
            span.extract()
        for a in li.find_all('a'):
            a.extract()
        sender = li.text.strip()

        details_response = requests.get(url='https://jwch.fzu.edu.cn/' + details_url, headers=headers)
        details_response.encoding = 'utf-8'
        details_soup = BeautifulSoup(details_response.text, 'html.parser')

        attachment_li_links = details_soup.select('ul[style="list-style-type:none;"] > li')
        if attachment_li_links:
            for li in attachment_li_links:
                attachment_name = li.find('a').text.strip()
                attachment_url = 'https://jwch.fzu.edu.cn/' + li.find('a')['href']
                # 打印后发现打印不出来下载次数，因此发现下载次数是动态加载的，分析XHR请求后发现会有一个response包含下载次数，而请求的url中包含id
                # id中含有一个没有用的nattach为了将其去掉我们从第8位开始取
                attachment_id = li.find('span')['id'][7:]
                attachment_download_url = 'https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid=' + attachment_id + '&owner=1744984858&type=wbnewsfile&randomid=nattach'
                # 观察后发现返回的是json字符串
                response_wb_show_times = requests.get(url=attachment_download_url, headers=headers)
                wb_show_times_text = response_wb_show_times.text
                wb_show_times = json.loads(wb_show_times_text)
                attachment_download_count = wb_show_times.get('wbshowtimes')
                # 将每个附件信息存储为一个单元素的列表
                attachment_info = f'{attachment_name} ({attachment_download_count}): {attachment_url}'
                file_name = os.path.basename(attachment_name)
                file_path = os.path.join(folder_path, file_name)
                response_download = requests.get(attachment_download_url)
                with open(file_path, 'wb') as file:
                    file.write(response.content)

                cursor.execute('''
                            INSERT INTO notifications (sender, title, date, details_url, attachments)
                            VALUES (%s, %s, %s, %s, %s)
                        ''', (sender, title, date, details_url, ''.join(attachment_info)))
                response.close()
                response_download.close()
                response_wb_show_times.close()
    print("成功爬取一页！")


if __name__ == "__main__":

    # 连接mysql数据库
    conn = mysql.connector.connect(host='localhost', user='root', password='102302', database='MyDepository')
    cursor = conn.cursor()

    truncate_table_query = "DROP TABLE IF NOT EXITS notifications"
    cursor.execute(truncate_table_query)
    # 创建数据表
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS notifications (
                id INT AUTO_INCREMENT PRIMARY KEY,
                sender VARCHAR(255),
                title VARCHAR(255),
                date VARCHAR(50),
                details_url VARCHAR(255),
                attachments TEXT
            )
    ''')

    url = 'https://jwch.fzu.edu.cn/jxtz.htm'
    crawl(url, cursor)

    url_2 = 'https://jwch.fzu.edu.cn/jxtz/183.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    response = requests.get(url=url_2, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    # 获取总页数
    a_list = soup.select('span[class="p_no"] > a')
    page_number = a_list[len(a_list) - 1].text

    # 获取总条数
    info_number = 0
    for i in range(1, int(page_number) + 1):
        li_list = soup.select('div[class="box-gl clearfix"] > ul > li')
        info_number += len(li_list)

    # 观察网址发现其他页网址位https://jwch.fzu.edu.cn/jxtz/i.htm，浅爬个10页吧
    for i in range(1, 10):
        new_url = 'https://jwch.fzu.edu.cn/jxtz/' + str(int(page_number) - i) + '.htm'
        crawl(new_url, cursor)

    print("总条数为：", info_number)
    print("总页数为：", page_number)

    response.close()
    conn.commit()
    conn.close()
