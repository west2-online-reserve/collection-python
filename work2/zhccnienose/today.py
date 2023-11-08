import requests
import datetime
import re
import pymysql
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 数据库连接初始化
    db = pymysql.connect(host='localhost',
                         user="root",
                         password="C310257813.",
                         database="TODAY")
    cursor = db.cursor()

    url_0 = "https://baike.baidu.com/cms/home/eventsOnHistory/10.json?_=1697469638605"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46"}
    dt = {"_": "1697469638605"}

    res = requests.get(url=url_0, headers=header)
    res.encoding = res.apparent_encoding
    res = res.json()

    today = datetime.date.today().strftime('%m%d')  # 获取当天日期
    tomonth = today[0:2]  # 当前月份

    list_today = res[tomonth][today]  # 获取当天数据
    re_title = r"[\u4e00-\u9fa5]"

    for item in list_today:
        title = ""
        for ch in re.findall(re_title, item["title"], re.MULTILINE):
            title += ch

        link = item["link"] + "?fromModule=today_on_history-lemma"

        detail_res = requests.get(url=link, headers=header)
        detail_res.encoding = detail_res.apparent_encoding
        detail_res = detail_res.text

        soup_detail = BeautifulSoup(detail_res, "lxml")
        detail = soup_detail.select('meta[name="description"]')[0]["content"]

        ins_today = "INSERT INTO `DAY` (`YEAR`, `TYPE`, `TITLE`, `DETAIL`) VALUES(%s, %s, %s,%s);"
        cursor.execute(ins_today, (item["year"], item["type"], title, detail))
        db.commit()

    db.close()
