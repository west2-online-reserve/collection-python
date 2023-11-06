# Author : AnnieHathaway
import requests
import re
import mysql.connector
from lxml import etree

def getCount(s):
    url2 = "https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp"
    ans = re.split(r'[(,")]',s)
    params = {
        'wbnewsid' : ans[1],
        'owner' : ans[2],
        'type' : 'wbnewsfile',
        'randomid' : 'nattach'
    }
    return requests.get(url=url2,params=params).json()['wbshowtimes']

# 连接到MySQL数据库
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="密码保密一下",
    database="west2"
)
# 创建游标
cursor = conn.cursor()

# 对教务处主页发送第一次请求
url = "https://jwch.fzu.edu.cn/jxtz.htm"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
resp1 = requests.get(url,headers=header)
page_code = resp1.text
html1 = etree.HTML(page_code)

# 获取总页数
total_page = html1.xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/span[1]/span[9]/a/text()")
print(total_page)

# 获取前五页链接
links = html1.xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/span[1]") # 定位
myLinks = []
for link in links:
    href_values = link.xpath(".//a/@href") # 匹配，生成String列表
    for href in href_values:
        full_link_1 = "https://jwch.fzu.edu.cn/" + href # 拼接link
        myLinks.append(full_link_1) # 将所有link存入myLinks
myLinks = myLinks[0:4] # 截取前四个
myLinks.insert(0,url) # 插入第一页

# 遍历每一页，对前五页每一页发送第二次请求
for myLink in myLinks:
    resp2 = requests.get(myLink,headers=header)
    resp2.encoding = "utf-8"
    link_code = resp2.text

    html2 = etree.HTML(link_code)

    # 解析一页中每一条通知的数据
    rows = html2.xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li") # 定位每一条通知

    # 遍历一页的20条通知
    title_set = []
    for row in rows:

        # 通知人
        name_elements = row.xpath("./text()")
        cleaned_name = [name.strip('\r\n ') for name in name_elements]
        name_set = [name.replace(',', '').replace('\'', '') for name in cleaned_name if name.strip()]
        print(len(name_set))
        # 日期
        date_elements = row.xpath("./span/text()")
        date_set = [date.strip('\r\n ') for date in date_elements]
        # 标题
        title_set = row.xpath("./a/text()")

        # 详情链接
        link_set = []
        annex_set = []
        count_set = []
        file_set = []
        link_elements = row.xpath("./a/@href")
        for link in link_elements:
            full_link_2 = "https://jwch.fzu.edu.cn/" + link
            link_set.append(full_link_2)

            # 对每一条通知的详情链接发送第三次请求
            resp3 = requests.get(full_link_2, headers=header)
            resp3.encoding = "utf-8"
            link_code2 = resp3.text
            html3 = etree.HTML(link_code2)
            details = html3.xpath('/html/body/div/div[2]/div[2]/form/div/div[1]/div/ul/li')

            file_set.append("None")
            annex_set.append("None")
            count_set.append(0)
            # 解析每一条通知内部的详情数据
            for detail in details:
                # 附件名
                annex = (detail.xpath(".//a/text()"))
                annex_set.pop(0)
                annex_set.append(str(annex))
                # 附件下载次数
                count = getCount(str(detail.xpath(".//span/script/text()")))
                count_set.pop(0)
                count_set.append(count)
                # 附件链接码
                files = detail.xpath(".//a/@href")
                file_set.pop(0)
                for f in files:
                    full_file = "https://jwch.fzu.edu.cn/" + f

                    response = requests.get(full_file)
                    if response.status_code == 200:
                        # 从URL中提取文件名
                        file_name = re.sub(r'[^a-zA-Z0-9_.-]', '_', full_file.split('/')[-1])

                        with open(file_name, 'wb') as file:
                            file.write(response.content)

                        print(f'文件 {file_name} 已保存。')
                    else:
                        print('无法下载文件。')
                    file_set.append(full_file)

        # 插入数据的SQL语句
        insert_data = "INSERT INTO fzu (name, date, link, title, file_name, file_count, file_link) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # 数据
        data = list(zip(name_set, date_set, link_set, title_set, annex_set, count_set, file_set))
        for d in data:
            # 执行SQL语句插入数据
            cursor.execute(insert_data, d)
resp1.close()
# 提交更改
conn.commit()
# 关闭游标和数据库连接
cursor.close()
conn.close()