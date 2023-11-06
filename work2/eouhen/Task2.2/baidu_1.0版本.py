# Author : AnnieHathaway
import requests
import mysql.connector
import time
import json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup


def database(year, kind, title, detail):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0623Hathaway",
        database="west2"
    )
    cursor = conn.cursor()
    insert_sql = "INSERT INTO baidu (year, kind, title, detail) VALUES (%s, %s, %s, %s);"
    values = (str(year), str(kind), title, detail)
    cursor.execute(insert_sql, values)

    conn.commit()
    cursor.close()
    conn.close()


def get_date_num(month):
    year = 2023
    first_day = datetime(year, month, 1)
    first_day.replace(day=1, month=month % 12 + 1, year=year if month % 12 != 12 else year + 1)
    last_day = first_day - timedelta(days=1)
    return last_day.day


def get_url(month):
    timestamp = int(time.time() * 1000)
    return f"https://baike.baidu.com/cms/home/eventsOnHistory/{month}.json?_={timestamp}"


def main():
    months_lst = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    for month in months_lst:
        url = get_url(month)
        response = requests.get(url).text
        data = json.loads(response)[month]
        days_lst = list(data.keys())
        days_lst.reverse()

        for day in days_lst:
            details = data[day]

            for detail in details:
                year = detail.get("year", "").strip()
                category = detail.get("type", "").strip()
                title = detail.get("title", "").strip()
                title = BeautifulSoup(title, "html.parser").get_text()
                content = detail.get("desc", "").strip()
                content = BeautifulSoup(content, "lxml").get_text()
                # print("年份：", year, "类型：", kind, "标题：", title, "内容：", content)
                database(year, category, title, content)


if __name__ == "__main__":
    main()
