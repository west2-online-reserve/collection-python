# 要求:

# 获取教务通知(最近100条即可，但需要获取总页数或条数)
# 提取通知信息中的“通知人”(如：质量办、计划科)、标题、日期、详情链接。
# 爬取通知详情的html，可能存在“附件”，提取附件名，附件下载次数，附件链接吗，有能力请尽可能将附件爬取下来。
# 上述内容一律要去除回车、括号等无用符号
# 把除附件外爬取到的数据存入数据库中

# 拿到网页源代码
# 用xpath提取有效信息
# 保存数据
import time
import requests
from lxml import etree
import json

for i in range(1, 6):
    if i == 1:
        url = 'https://jwch.fzu.edu.cn/jxtz.htm'
    else:
        url = 'https://jwch.fzu.edu.cn/jxtz/{}.htm'.format(str(185 - i))
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289'}
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'
    resp = resp.content
    # print(resp)
    # 对代码进行分析
    # 先把变量放到解析器:分析容器里面
    html = etree.HTML(resp)
    # /html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li[1]
    # /html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li[2]
    # /html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li[3]
    divs = html.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li')
    for div in divs:
        # /html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li[1]/a

        title = div.xpath('./a/text()')[0]
        # print(title)
        time.sleep(1)
        # 获取通知人信息
        # /html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li[1]/text()
        # /html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li[2]/text()
        Name = div.xpath('./text()')[0]
        print(Name)
        # 获取日期
        # /html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li[3]/span
        # /html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li[2]/span
        # /html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li[6]/span
        TM = div.xpath('./span/text()')[0]
        # print(TM)
        # 获取链接
        # /html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/ul/li[6]/a
        # https://jwch.fzu.edu.cn/info/1037/12996.htm
        # https://jwch.fzu.edu.cn/info/1039/12999.htm
        # 获取a标签下的href
        href = div.xpath('./a/@href')[0]
        # print(href)
        # https://jwch.fzu.edu.cn/info/1037/12996.htm
        # 链接拼接
        href2 = 'https://jwch.fzu.edu.cn/' + href
        # print(href2)
        time.sleep(2)
        # 翻页问题
        # http://journal.whu.edu.cn/news/index 第一页
        # http://journal.whu.edu.cn/news/index/page/2
        # http://journal.whu.edu.cn/news/index/page/3

        with open(r'福大爬取通知.txt', 'a', encoding='utf-8') as f:
            f.write('{{{},{},{},{}}}'.format(str(Name), str(title), str(TM), str(href2)))
            f.write('\n')

