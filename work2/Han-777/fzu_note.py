# """爬取福大教务通知 https://jwch.fzu.edu.cn/jxtz.htm
#
# 要求:
#
# 获取教务通知(最近100条即可，但需要获取总页数或条数)
# 提取通知信息中的“通知人”(如：质量办、计划科)、标题、日期、详情链接。
# 爬取通知详情的html，可能存在“附件”，提取附件名，附件下载次数，附件链接吗，有能力请尽可能将附件爬取下来。
# 上述内容一律要去除回车、括号等无用符号
# 把除附件外爬取到的数据存入数据库中"""
import re

import pymysql
import requests
from lxml import etree
from selenium import webdriver


class Spider:
    required_NoteNum = 100
    note_Title = []
    note_Author = []
    note_Date = []
    note_Link = []
    note_data = []
    note_file = []

    def __init__(self):
        self.url = 'https://jwch.fzu.edu.cn/jxtz.htm'
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
        page_Text = self.send_request(None)
        self.get_Data(page_Text)
        self.get_file()
        self.insert_db()

    @classmethod
    def get_PageNum(cls, page_text):
        all_page_num = re.search(r'<a href="jxtz/1.htm">(\d{3})</a>', page_text, re.S).group(1)
        return all_page_num

    @classmethod
    def get_Data(cls, page_text):
        id = 0
        print(f'总页数： {cls.get_PageNum(page_text)}')
        tree = etree.HTML(page_text)
        while id <= cls.required_NoteNum:
            li_list = tree.xpath('//ul[@class="list-gl"]/li')
            for li in li_list:
                id += 1
                temp_list = [id]
                if id <= cls.required_NoteNum:
                    # Date
                    Date = re.findall(r'(\d\d\d\d-\d\d-\d\d)', str(li.xpath('./span/text()')[0]), re.S)
                    temp_list.append(Date)
                    # title
                    note_title = li.xpath('./a/@title')[0]
                    temp_list.append(note_title)
                    # Author
                    Author = re.findall(r'【(.*?)】', str(li.xpath('./text()')), re.S)
                    temp_list.append(Author)
                    # Link
                    if li.xpath('./a/@href')[0][0] == '.':
                        info_link = "https://jwch.fzu.edu.cn/" + li.xpath('./a/@href')[0][2:]
                    elif li.xpath('./a/@href')[0][0] == 'i':
                        info_link = "https://jwch.fzu.edu.cn/" + li.xpath('./a/@href')[0]
                    else:
                        info_link = li.xpath('./a/@href')
                    temp_list.append(info_link)
                    cls.note_data.append(temp_list)
                else:
                    break
            turnToPage_Num = tree.xpath('//span[@class="p_no_d"]/text()')[0]
            turnPage_url = 'https://jwch.fzu.edu.cn/jxtz/' + str(184 - int(turnToPage_Num)) + '.htm'
            page_Text = cls().send_request(turnPage_url)
            tree = etree.HTML(page_Text)
        print(cls.note_data)

    @classmethod
    def get_file(cls):
        file_id = 1
        for u_list in cls.note_data:
            page_Text = cls().send_request(u_list[4])
            if re.search(r'附件【', page_Text):
                sid_list = re.findall(r'getClickTimes\((\d*?),', page_Text)
                tree = etree.HTML(page_Text)
                li_list = tree.xpath('//ul[@style="list-style-type:none;"]/li')
                for li, sid in zip(li_list, sid_list):
                    js_url = f'https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid={sid}&owner=1744984858&type=wbnewsfile&randomid=nattach '
                    file_Name = li.xpath('./a/text()')[0]
                    download_Num = requests.get(js_url).json().get('wbshowtimes')
                    file_Link = "https://jwch.fzu.edu.cn" + li.xpath('./a/@href')[0]
                    # file_list = [file_id, {"附件名:": file_Name, '下载次数:': download_Num, '附件链接:': file_Link}]
                    temp_list = [file_id, file_Name, download_Num, file_Link]
                    file_id += 1
                    cls.note_file.append(temp_list)
        print(cls.note_file)

    @classmethod
    def insert_db(cls):
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database='db_python',
                               charset='utf8')
        cursor = conn.cursor()
        insert_data_sql = "INSERT INTO `task1_data` (`id`, `date`, `title`, `author`, `brief`) VALUES(%s, %s, %s, %s, %s);"
        insert_file_sql = "INSERT INTO `task1_file` (`fileId`, `fileName`, `downloadNum`, `fileLink`) VALUES(%s, %s, %s, %s);"

        for data in cls.note_data:
            cursor.execute(insert_data_sql, (data[0], data[1], data[2], data[3], data[4]))
            conn.commit()
        for file in cls.note_file:
            cursor.execute(insert_file_sql, (file[0], file[1], file[2], file[3]))
            conn.commit()

        cursor.close()
        conn.close()


if __name__ == '__main__':
    fzu_Note = Spider()
    fzu_Note.run()
