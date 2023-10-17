import requests
import re
from bs4 import BeautifulSoup
import pymysql

if __name__ == "__main__":
    # 连接数据库webwork
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='C310257813.',
                         database='webwork')
    cursor = db.cursor()

    url_0 = "https://jwch.fzu.edu.cn"
    # 通知首页
    url_1 = "https://jwch.fzu.edu.cn/jxtz.htm"
    # 附件url
    url_annex = "https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid=13053671&owner=1744984858&type=wbnewsfile&randomid=nattach"
    header = {
        "User - Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60"
    }
# 第一页数据爬取
    res_head = requests.get(url=url_1, headers=header)  # 首页
    res_head.encoding = res_head.apparent_encoding
    # print(res.encoding)
    text_head = res_head.text

    soup_head = BeautifulSoup(text_head, "lxml")  # 首页源码数据
    tot_page = soup_head.select(".p_no > a")[-1].string  # 总页数
    list_head = soup_head.select(" ul.list-gl > li")  # 首页通知主体

    for item in list_head:
        notice_title = item.a["title"]  # 通知标题
        notice_id = url_0 + "/" + item.a["href"]  # 通知详情链接
        notice_er = re.findall(r'【.*?】', str(item.text), re.MULTILINE)[0][1:-1]  # 通知人
        notice_date = re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', item.text, re.MULTILINE)[0]  # 通知日期

        # 在表NOTICE中插入数据 TITLE, ID, ER, DATE
        # print(notice_title)
        ins_not = "INSERT INTO `NOTICE` (`TITLE`, `ID`, `ER`, `DATE`) VALUES(%s, %s, %s, %s);"
        cursor.execute(ins_not, (notice_title, notice_id, notice_er, notice_date))
        db.commit()

# 后续页面数据爬取
    for i in range(int(tot_page) - 1, int(tot_page) - 5, -1):
        url = "https://jwch.fzu.edu.cn/jxtz/" + str(i) + ".htm"
        res_page = requests.get(url=url, headers=header)
        res_page.encoding = res_page.apparent_encoding
        text_page = res_page.text

        soup_page = BeautifulSoup(text_page, "lxml")
        list_page = soup_page.select("ul.list-gl > li")

        for item in list_page:
            notice_title = item.a["title"]  # 通知标题
            notice_id = url_0 + re.findall(r'/.*', item.a["href"], re.MULTILINE)[0]  # 通知详情链接
            notice_er = re.findall(r'【.*?】', item.text, re.MULTILINE)[0][1:-1]  # 通知人
            notice_date = re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', item.text, re.MULTILINE)[0]  # 通知日期

            # 在表NOTICE中插入数据 TITLE, ID, ER, DATE
            ins_not = "INSERT INTO `NOTICE` (`TITLE`, `ID`, `ER`, `DATE`) VALUES(%s, %s, %s, %s);"
            cursor.execute(ins_not, (notice_title, notice_id, notice_er, notice_date))
            db.commit()

            res_detail = requests.get(url=notice_id, headers=header)  # 获取详情页数据
            res_detail.encoding = res_detail.apparent_encoding
            text_res_detail = res_detail.text
            soup_detail = BeautifulSoup(text_res_detail, "lxml")

            if soup_detail.find('ul', style='list-style-type:none;') is not None:  # 存在附件
                list_li = soup_detail.select("ul[style='list-style-type:none;'] > li")

                for item_li in list_li:
                    annex_name = item_li.a.string  # 附件名称
                    annex_id = url_0+item_li.a["href"]  # 附件链接
                    annex_time = requests.get(url_annex).json().get("wbshowtimes")  # 附件下载次数

                    # print("名称:", annex_name, " 链接:", annex_id," 下载次数:",annex_time)
                    # 在表ANNEX中插入数据 NAME,ID,TIME
                    ins_annex = "INSERT INTO `ANNEX` (`NAME`, `ID`, `TIME`) VALUES(%s, %s, %s);"
                    cursor.execute(ins_annex, (annex_name, annex_id, annex_time))
                    db.commit()

    db.close()
    print("Over!!!")
