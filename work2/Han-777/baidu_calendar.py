"""要求:

获取一年内每天的历史上的今天发生了什么，包括年份，事件类型(birth、death等)，标题，简要内容
上述内容一律要去除回车、括号等无用符号
把爬取到的数据存入数据库中"""

import pymysql
import requests
from lxml import etree
from selenium import webdriver
from time import sleep


class Spider:
    data = []

    def __init__(self):
        self.url = 'https://baike.baidu.com/calendar/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'Connection': 'close'
        }

    def send_request(self, turnPage_url):
        if turnPage_url is None:
            res = requests.get(url=self.url, headers=self.headers)
        else:
            res = requests.get(url=turnPage_url, headers=self.headers)
        res.encoding = 'utf-8'
        return res.text

    def run(self):
        self.get_Data(2)
        self.insert_db()

    @classmethod
    def get_Data(cls, dateNum):
        id = 0
        bro = webdriver.Chrome(executable_path='./chromedriver.exe')
        bro.get('https://baike.baidu.com/calendar/')
        js = "var q=document.documentElement.scrollTop=5000"
        bro.execute_script(js)
        sleep(1)
        page_text = bro.page_source
        tree = etree.HTML(page_text)
        dd_list = tree.xpath('//dl[@class="events"]/dd')
        for dd in dd_list:
            id += 1
            temp_list = [id]
            # year
            data_year = dd.xpath('./div[@class="year"]/text()')[0]
            temp_list.append(data_year)
            # type
            event_type = dd.xpath('.//div[@class="event_tit"]/text()')
            temp_list.append(event_type[-1])
            # title
            div_list = dd.xpath('.//div[@class="event"]//div[@class="event_tit"]')
            for div in div_list:
                event_title = div.xpath('string(.)').strip()
                temp_list.append(event_title)
            # brief
            div_list = dd.xpath('.//div[@class="event"]/div[@class="event_cnt"]')
            for div in div_list:
                event_brief = div.xpath('string(.)').strip()
                temp_list.append(event_brief)
            cls.data.append(temp_list)
        print(cls.data)
        sleep(1)
        bro.quit()

    @classmethod
    def insert_db(cls):
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database='db_python',
                               charset='utf8')
        cursor = conn.cursor()
        insert_data_sql = "INSERT INTO `task2` (`id`, `year`, `type`, `title`, `brief`) VALUES(%s, %s, %s, %s, %s);"

        for data in cls.data:
            cursor.execute(insert_data_sql, (data[0], data[1], data[2], data[3], data[4]))
            conn.commit()

        cursor.close()
        conn.close()


if __name__ == '__main__':
    calendar = Spider()
    calendar.run()
