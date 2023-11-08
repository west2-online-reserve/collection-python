import requests
import re
import pymysql
import time
import calendar


def get_url():
    timestamp = int(time.time()*1000)
    timestamp_str = str(timestamp)
    get_url_list = []
    num_str_list = []
    for month in range(1, 13):
        format_num = f"{month:02d}"
        format_num_str = str(format_num)
        num_str_list.append(format_num_str)
        detail_url = ("https://baike.baidu.com/cms/home/eventsOnHistory/"+format_num_str+".json?_="+timestamp_str)
        get_url_list.append(detail_url)
    return get_url_list, num_str_list


def get_date_num(month):
    year = 2023
    month_day_num = calendar.monthrange(year, month)[1]
    return month_day_num


def database(year, category, title, detail):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='s88159868',
        database='work2'
    )
    cursor = conn.cursor()
    year_str = str(year)
    category_str = str(category)
    title_str = str(title)
    detail_str = str(detail)
    sql = f"INSERT INTO baidu_history (year, category, title, detail) VALUES ('{year_str}', '{category_str}', '{title_str}', '{detail_str}');"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


detail_url_list, num_str_list = get_url()
# print(detail_url_list, num_str_list)
# date_num_list = get_date_num()
# print(date_num_list)
for i in range(0, 12):
    detail_url = detail_url_list[i]
    # print(detail_url)
    url_resp = requests.get(detail_url).json()
    # print(url_resp)
    # print(f"{num_str_list[i]}")
    page_info = url_resp.get(f"{num_str_list[i]}")
    # print(page_info)
    date_num = get_date_num(i+1)
    # print(date_num)
    num = num_str_list[i]
    for a in range(1, date_num+1):
        format_a = f"{a:02d}"
        detail_info = page_info.get(f"{num}"+f"{format_a}")
        # print(f"{num}"+f"{format_a}")
        for info in detail_info:
            # print(info)
            year = info.get("year")
            s1_year = re.sub(r'\s', '', year)
            category = info.get("type")
            s1_category = re.sub(r'\s', '', category)
            title = info.get("title")
            s1_title = re.sub(r'<.*?>', '', title)
            s2_title = re.sub(r'\s|\'|<a[^>]*>|href="[^"]*"', '', s1_title)
            content = info.get("desc")
            s1_content = re.sub(r'<.*?>', '', content)
            s2_content = re.sub(r'\s|\'', '', s1_content)
            print("年份：", s1_year, "类型：", s1_category, "标题：", s2_title, "简要内容：", s2_content)
            database(s1_year, s1_category, s2_title, s2_content)

