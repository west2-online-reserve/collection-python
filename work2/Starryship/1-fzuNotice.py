'''爬取福大教务通知 https://jwch.fzu.edu.cn/jxtz.htm

要求:

获取教务通知(最近100条即可，但需要获取总页数或条数)
提取通知信息中的“通知人”(如：质量办、计划科)、标题、日期、详情链接。
爬取通知详情的html，可能存在“附件”，提取附件名，附件下载次数，附件链接吗，有能力请尽可能将附件爬取下来。
上述内容一律要去除回车、括号等无用符号
把除附件外爬取到的数据存入数据库中'''

import requests
import re
from bs4 import BeautifulSoup
import json
from pymysql import connect



def main2(ur):
    """爬取附件"""

    response = requests.get(url=ur, headers=headers).content.decode("utf8")

    soup = BeautifulSoup(response, "lxml")

    li = soup.select(".xl_main li")
    for i in range(len(li)):
        file_href = "https://jwch.fzu.edu.cn" + li[i].find("a")["href"]
        file_name = li[i].find("a").text

        ll = re.findall(r"\d+", file_href)
        u = 'https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid=' + ll[1] + '&owner=' + ll[
            0] + '&type=wbnewsfile&randomid=nattach'
        ui = json.loads(requests.get(url=u, headers=headers).text)

        sql2 = "insert into files (name,download_num,href) values('%s','%s','%s')" % (file_name, ui['wbshowtimes'], file_href)

        cursor.execute(sql2)
        con.commit()


        # print(file_href, file_name, ui['wbshowtimes'])


def main():
    """获取教务处通知"""

    #统计获取通知的条数
    count = 0
    #
    for j in range(5):
        if j == 0:
            url = "https://jwch.fzu.edu.cn/jxtz.htm"
        else:
            url = "https://jwch.fzu.edu.cn/jxtz{}.htm".format("/" + str(184 - j))

        response = requests.get(url=url, headers=headers).content.decode("utf8")

        soup = BeautifulSoup(response, "lxml")

        li_list = soup.select(".list-gl li")
        for i in range(len(li_list)):
            #获取详情链接
            href ="https://jwch.fzu.edu.cn/"+ li_list[i].find("a")["href"]
            #获取时间
            time = li_list[i].find("span").string
            if time==None:
                time=li_list[i].find("font").string
            #获取通知人
            agency = re.findall(r"【(.*?)】", li_list[i].text)[0]
            #获取标题
            title=li_list[i].find("a")["title"]
            count+=1

            main2(href)

            #将数据读入数据库
            sql2 = "insert into notices (agency,title,time,href) values('%s','%s','%s','%s')" % (agency,title,time,href)

            cursor.execute(sql2)
            con.commit()
    print("获取通知的条数为：{}条".format(count))


if __name__ == "__main__":

    headers = {"User-Agent":
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}

    #连接数据库
    con = connect(host='127.0.0.1', port=3306, user='root', password='root', charset='utf8')
    #创建游标
    cursor = con.cursor()
    #创建数据库
    cursor.execute("create database if not exists xing DEFAULT CHARSET utf8 COLLATE utf8_general_ci")
    #使用数据库
    cursor.execute("use xing")

    #创建通知表
    sql = """
    create table notices(
        id int not null auto_increment primary key,
        agency varchar(128),
        title varchar(128),
        time varchar(128),
        href varchar(128)
    )default charset=utf8
        """
    #创建爬取附件信息的表
    sql3 = """
    create table files(
        id int not null auto_increment primary key,
        name varchar(128),
        download_num varchar(128),
        href varchar(128)
    )default charset=utf8
        """

    cursor.execute(sql)
    cursor.execute(sql3)

    #调用爬取通知的函数
    main()

    #关闭游标
    cursor.close()
    #关闭连接
    con.close()