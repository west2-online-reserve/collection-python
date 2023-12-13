import sys
import time
import requests
import re
import pymysql

group = []  # 作者来源
title = []  # 文章标题
net = []  # 详情链接
txt = ''
sum = 0
page = ''  # 总页数
urls = []  # 附件链接
ttime = []  # 文章发表时间
downtimes = []  # 文件下载次数
name = []  # 文件名
suser = input('请输入MySQL的用户名user:')
spassword = input('请输入MySQL用户"' + suser + '"的密码:')
db = pymysql.connect(host='localhost',user=suser,password=spassword,database='PYTHON')
c = db.cursor()


def getlist(url):
    global group, title, net, page, txt, sum
    returns = requests.get(url)  # 发送一个请求
    returns.encoding = 'utf-8'  # 防止出现乱码
    txt = returns.text  # 取出其中的文本
    groups = re.findall("\u3010.*?\u3011", txt)  # 获取各个文章来自的部门
    titles_first = re.findall(".htm\" target=\"_blank\" title=\".*?\"", txt)  # 使用正则表达式对文本进行第一次过滤
    titles_second = ''  # 初始化一个字符串变量用来存储第二遍过滤的文本
    for temp in titles_first:  # 进行第二次过滤
        titles_second += re.findall("title=\".*?\"", temp)[0]
    titles = re.findall("\".*?\"", titles_second)  # 最后一次过滤
    nets_first = re.findall("<a href=\".*info/..../.*?.htm\"", txt)  # 获取详细网址链接并过滤
    nets_second = ''
    for temp in nets_first:
        nets_second += re.findall("\".*?\"", temp)[0]
    nets = re.findall("\".*?\"", nets_second)
    for temp in range(0, len(groups)):  # 去除作者组中的冗余括号
        groups[temp] = groups[temp].strip('【')
        groups[temp] = groups[temp].strip('】')
    for temp in range(0, len(titles)):  # 去除标题中冗余的引号
        titles[temp] = titles[temp].strip('"')
    for temp in range(0, len(nets)):  # 去除网址中冗余的引号
        nets[temp] = nets[temp].strip('"')
        nets[temp] = 'https://jwch.fzu.edu.cn/' + nets[temp].strip('../')
    group += groups
    title += titles
    net += nets
    sum += len(nets)


def getinfo(url):
    detailsAll = requests.get(url)
    detailsAll.encoding = 'utf-8'
    detailsText = detailsAll.text
    ttime.append(re.findall("发布时间：....-..-..", detailsText)[0].strip("发布时间："))
    if len(re.findall('\u5df2\u4e0b\u8f7d', detailsText)) == 0:
        urls.append('无')
        name.append("无附件")
        downtimes.append('0')
        return
    filename = re.findall("\">.*?</a>】已下载", detailsText)
    ajaxUrls = re.findall("\([0-9]{7,8}", detailsText)
    downloadnet = re.findall("【<a href=\".*?\"", detailsText)
    numbers = len(ajaxUrls)
    dlts = ''
    flnms = ''
    dlnts = ''
    for i in range(0, numbers):
        ajaxUrls[i] = ajaxUrls[i].strip('(')
        dlt = requests.get(
            'https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp?wbnewsid=' + ajaxUrls[
                i] + '&owner=1744984858&type=wbnewsfile&randomid=nattach')
        times = dlt.text
        downloadTimes = ''
        for u in range(15, 19):
            downloadTimes += times[u]
        downloadTimes = (downloadTimes.strip("\"")).strip(",")
        dlts += (downloadTimes + ';')
        downloadnet[i] = downloadnet[i].strip("【<a href=\"")
        downloadnet[i] = downloadnet[i].strip("\"")
        downloadnet[i] = 'https://jwch.fzu.edu.cn' + downloadnet[i]
        downloadTimes = downloadTimes.strip(",")
        filename[i] = filename[i].strip("\">附件：")
        filename[i] = filename[i].strip("</a>】已下载")
        filename[i] = filename[i].strip("1：")
        filename[i] = filename[i].strip("2：")
        filename[i] = filename[i].strip("3：")
        filename[i] = filename[i].strip("4：")
        filename[i] = filename[i].strip("5：")
    for u in filename:
        flnms += (u + ";")
    for u in downloadnet:
        dlnts += (u + ";")
    name.append(flnms.strip(";"))
    urls.append(dlnts.strip(";"))
    downtimes.append(dlts.strip(";"))


c.execute("TRUNCATE TABLE python.information;")
db.commit()
getlist('https://jwch.fzu.edu.cn/jxtz.htm')
pages = re.findall("...\.htm\">2", txt)  # 从这里开始4行取页码总数
for i in range(0, 3):
    page += pages[0][i]
page = int(page) + 1
print('总页数为', page)
for i in range(1, page):  # 循环获取前100个
    print("\r", end="")
    print("获取信息进度: {}%: ".format(int(((i + 1) / page) * 100)), "▓" * (int(((i + 1) / page)*100) // 2), end="")
    sys.stdout.flush()
    getlist('https://jwch.fzu.edu.cn/jxtz/' + str(int(page) - i) + '.htm')
print('\n')
for i in range(0, page*20-1):
    getinfo(net[i])  # 详情链接50 标题100 附件链接120
    if (urls[i] == '无'):
        c.execute(
            "insert into python.information (title,GR,net,time,downloadtimes,acc,file,filename) values('" + title[
                i] + "','" + group[
                i] + "','" + net[i] + "','" + ttime[i] + "','" + downtimes[i] + "','无','" + urls[i] + "','" + name[
                i] + "');")
    else:
        c.execute(
            "insert into python.information (title,GR,net,time,downloadtimes,acc,file,filename) values('" + title[
                i] + "','" + group[
                i] + "','" + net[i] + "','" + ttime[i] + "','" + downtimes[i] + "','有','" + urls[i] + "','" + name[
                i] + "');")
    db.commit()
    print("\r", end="")
    print("存储到数据库进度: {}% ".format(int(((i + 1) / sum) * 100)), "▓" * int((((i + 1) / sum) * 100) // 2), end="")
    sys.stdout.flush()
db.close()
c.close()
print("\n数据已保存至数据库")
