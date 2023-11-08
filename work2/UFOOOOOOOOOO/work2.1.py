from lxml import etree
import requests
import re
import pymysql


def select_page(num):
    urls_list = []
    for i in range(0, 5):
        if i == 0:
            url = ("https://jwch.fzu.edu.cn/jxtz.htm")
            urls_list.append(url)
        if i != 0:
            page_num = num - i
            page_num_str = str(page_num)
            url = ("https://jwch.fzu.edu.cn/jxtz/"+page_num_str+".htm")
            urls_list.append(url)
    return urls_list


def select_detail_page(url):
    detail_page_url_list = []
    # print(url)
    detail_page_resp = requests.get(url, headers=headers).text
    # print(detail_page_resp)
    detail_page_html = etree.HTML(detail_page_resp)
    detail_page = detail_page_html.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li/a/@href')
    # print(detail_page)
    for i in range(0, 19):
        detail_page_url = ("https://jwch.fzu.edu.cn/"+detail_page[i])
        # print(detail_page_url)
        detail_page_url_list.append(detail_page_url)
        i += 1
    return detail_page_url_list


def fujian(page_html):
    check = page_html.xpath("/html/body/div/div[2]/div[2]/form/div/div[1]/div/ul/text()")
    if check:
        num_list = []
        detail_file_download_url_list = []
        detail_file_name_list = page_html.xpath("/html/body/div/div[2]/div[2]/form/div/div[1]/div/ul/li/a/text()")
        detail_file_download_list = page_html.xpath("/html/body/div/div[2]/div[2]/form/div/div[1]/div/ul/li/a/@href")
        nums = page_html.xpath("/html/body/div/div[2]/div[2]/form/div/div[1]/div/ul/li")
        for num_html in nums:
            num = num_html.xpath("string(span)")
            wbnewsid = re.search(r'getClickTimes\((\d*?),', num).group(1)
            url = f'https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid={wbnewsid}&owner=1744984858&type=wbnewsfile&randomid=nattach'
            num = requests.get(url).json().get('wbshowtimes')
            print(type(requests.get(url).json()))
            print(requests.get(url).json())
            print(type(requests.get(url)))
            num_list.append(num)
        for detail_file_download in detail_file_download_list:
            detail_file_download_url = ("https://jwch.fzu.edu.cn/"+detail_file_download)
            detail_file_download_url_list.append(detail_file_download_url)
        print("共有", len(detail_file_download_url_list), "个附件:")
        for i in range(len(detail_file_download_url_list)):
            print("附件", i+1, "：", detail_file_name_list[i], "\n", "附件下载链接：", detail_file_download_url_list[i], "\n",
                  "附件下载次数：", num_list[i])
        # print(detail_file_name_list, detail_file_download_url_list, num_list)
        return detail_file_name_list, detail_file_download_url_list, num_list
    else:
        print("无附件")


def database(name, title, date, url, detail_name=None, detail_url=None, download_times=None):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='s88159868',
        database='fzu_jwc_information'
    )
    cursor = conn.cursor()
    name_str = str(name)
    title_str = str(title)
    date_str = str(date)
    url_str = str(url)
    if detail_name is not None:
        detail_name = [str(name) for name in detail_name]
        detail_url = [str(url) for url in detail_url]
        download_times = [str(time) for time in download_times]
        name_string = '\\'.join(detail_name)
        url_string = '\\'.join(detail_url)
        times_string = '\\'.join(download_times)
        sql1 = f"INSERT INTO notice_information (name, title, date, url, detail_name, detail_url, download_times) VALUES ('{name_str}', '{title_str}', '{date_str}', '{url_str}', '{name_string}', '{url_string}', '{times_string}');"
        # print(sql1)
        cursor.execute(sql1)
        conn.commit()
    else:
        sql2 = f"INSERT INTO notice_information (name, title, date, url, detail_name, detail_url, download_times) VALUES ('{name_str}', '{title_str}', '{date_str}', '{url_str}', '{detail_name}', '{detail_url}', '{download_times}');"
        cursor.execute(sql2)
        conn.commit()
    cursor.close()
    conn.close()


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60"
}
n_num_url1_rep = requests.get("https://jwch.fzu.edu.cn/jxtz.htm", headers=headers).text
html_num_url1 = etree.HTML(n_num_url1_rep)
n_num = html_num_url1.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/span[1]/span[9]/a/text()')
# print(n_num[0])
int_n_num = int(n_num[0])
print("总页数：", int_n_num)
urls = select_page(int_n_num)
# print(urls[1])
for i in range(0, 5):
    detail_urls = select_detail_page(urls[i])
    # print(detail_urls)
    for i in range(0, 19):
        detail_rep = requests.get(detail_urls[i], headers=headers).content
        detail_html = etree.HTML(detail_rep, parser=etree.HTMLParser(encoding='utf8'))
        # 解决中文乱码
        detail_name = detail_html.xpath("/html/body/div/div[2]/div[1]/p/a[3]/text()")
        detail_title = detail_html.xpath("/html/body/div/div[2]/div[2]/form/div/div[1]/div/div[1]/h4/text()")
        detail_date = detail_html.xpath("/html/body/div/div[2]/div[2]/form/div/div[1]/div/div[2]/div[1]/span[1]/text()")
        print("通知人：", detail_name[0])
        print("通知标题：", detail_title[0])
        print(detail_date[0])
        print("详情链接：", detail_urls[i])
        result = fujian(detail_html)
        if result is not None:
            database(detail_name[0], detail_title[0], detail_date[0], detail_urls[i], result[0], result[1], result[2])
        else:
            database(detail_name[0], detail_title[0], detail_date[0], detail_urls[i])
        print()
        i += 1




