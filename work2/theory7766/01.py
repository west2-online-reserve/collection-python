from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import requests
import json
from pymysql import Connection


# 实例化浏览器对象
def getChrome():
    # selenium 无头浏览器
    options = Options()
    options.add_argument('--headless')  # 不提供可视化界面
    options.add_argument('--disable-gpu')  # 用于规避bug
    driver = webdriver.Chrome(options=options)
    return driver

# 获取页面源码数据
def getPageText(url):
    driver = getChrome()
    driver.get(url)
    pageText = driver.page_source
    return pageText


# 使用requests和xpath获取总页数
def getPageSum(url):
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/116.0.0.0 Safari/537.36 '
    }
    response = requests.get(url=url, headers=headers)
    # 解决中文乱码
    response.encoding = response.apparent_encoding
    pageText = response.text
    tree = etree.HTML(pageText)
    page = tree.xpath('//span[@class="p_no"][5]/a/text()')[0]
    print("总页数：", page)
    return page


# 使用selenium获取附件名，附件链接，附件下载次数,并且下载附件
def getFile(url):
    pageText = getPageText(url)
    tree = etree.HTML(pageText)
    file_list = []
    li_list = tree.xpath('//div[@class="xl_main"]/ul/li')
    if li_list:
        for li in li_list:
            annexName = li.xpath('normalize-space(./a/text())')
            downloadNum = li.xpath('./span//text()')[0]
            downloadLink = 'https://' + li.xpath('./a/@href')[0]
            file_list.append({"附件名字": annexName, "下载次数": downloadNum, "下载链接": downloadLink})
        return file_list
    else:
        return file_list


# 创建表
def createTable():
    con = None
    try:
        con = Connection(
            host="localhost",  # 主机名
            port=3306,  # 端口
            user="root",  # 用户名
            password="Lucy0311@",  # 密码
            database="db1",  # 指定操作的数据库
            autocommit=True
        )
        # 若未在数据库db1中创建表news则创建
        createNewsSql = """
                    CREATE TABLE IF NOT EXISTS `news` (
                    `notifier` VARCHAR (10) NOT NULL ,
                    `title` VARCHAR (200) NOT NULL ,
                    `date` VARCHAR(15) NOT NULL,
                    `link` VARCHAR (200) NOT NULL,
                    PRIMARY KEY(`link`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
                 """
        createFileSql = """
                        CREATE TABLE IF NOT EXISTS `file` (
                        `annexName` VARCHAR (200) NOT NULL,
                        `downloadNum` VARCHAR (10) NOT NULL,
                        `downloadLink`  VARCHAR (500) NOT NULL,
                        PRIMARY KEY(`downloadLink`)
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
                        """
        cursor = con.cursor()
        cursor.execute(createNewsSql)
        cursor.execute(createFileSql)
        # 删除原有数据
        deleteSql = "DELETE FROM `news`"
        cursor.execute(deleteSql)
        deleteSql = "DELETE FROM `file`"
        cursor.execute(deleteSql)
    except Exception as e:
        print("异常1：", e)
    finally:
        if con:
            con.close()

# 将除附件之外的信息存入数据库
def insertDb(info_list):
    # 创建数据库链接
    con = None
    try:
        con = Connection(
            host="localhost",  # 主机名
            port=3306,  # 端口
            user="root",  # 用户名
            password="Lucy0311@",  # 密码
            database="db1",  # 指定操作的数据库
            autocommit=True  # insert时使用
        )
        insertNewsSql = "INSERT INTO `news`(`notifier`,`title`,`date`,`link`) VALUES (%s, %s, %s, %s);"
        insertFileSql = "INSERT INTO `file`(`annexName`,`downloadNum`,`downloadLink`) VALUES (%s, %s, %s);"
        cursor = con.cursor()
        for info in info_list:
            print(json.dumps(info, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':')))
            cursor.execute(insertNewsSql, (info["通知人"], info["标题"], info["日期"], info["链接"]))
            for file in info["附件下载"]:
                cursor.execute(insertFileSql, (file["附件名字"], file["下载次数"], file["下载链接"]))
        cursor.close()
    except Exception as e:
        print("异常2：", e)
    finally:
        if con:
            con.close()


# 使用requests和xpath获取每篇文章通知人，标题，日期，详情链接
def crawData(url):
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/116.0.0.0 Safari/537.36 '
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    pageText = response.text
    tree = etree.HTML(pageText)
    message_li_list = tree.xpath('//div[@class="box-gl clearfix"]/ul/li')
    info_list = []
    for li in message_li_list:
        # 通知人
        notifier = li.xpath('normalize-space(./text()[2])')
        # 去除括号
        notifier = notifier[1:-1]
        # 标题
        title = li.xpath('normalize-space(./a/@title)')
        # 日期
        date = li.xpath('./span//text()')
        if len(date) == 1:
            date = li.xpath('normalize-space(./span//text())')
        else:
            date = li.xpath('normalize-space((./span//text())[2])')
        # 详情链接
        newurl = 'https://jwch.fzu.edu.cn/' + li.xpath('./a/@href')[0]
        file_list = getFile(newurl)
        info_dict = {"通知人": notifier, "标题": title, "日期": date, "链接": newurl, "附件下载": file_list}
        info_list.append(info_dict)
        print(json.dumps(info_dict, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':')))
    insertDb(info_list)


def main():
    url = "https://jwch.fzu.edu.cn/jxtz.htm"
    # 获取总页数
    pageSum = getPageSum(url)
    # 建表
    createTable()
    # 获得第一页数据
    crawData(url)
    # 获取第2到第4页数据并存进数据库中
    for i in range(1, 5):
        url = "https://jwch.fzu.edu.cn/jxtz/" + str(int(pageSum) - i) + ".htm"
        crawData(url)


if __name__ == '__main__':
    main()
