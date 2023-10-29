import re
import requests
import bs4
import pymysql

print("请输入本机MySQL的root用户密码：", end='')  # 不检查正确性
password = input()
connection = pymysql.connect(host='localhost', user='root', password=password)
cursor = connection.cursor()
cursor.execute('drop database if exists notices')
cursor.execute('create database notices charset=utf8')
connection = pymysql.connect(host='localhost', user='root', password=password, database='notices', charset='utf8')
cursor = connection.cursor()

cursor.execute('''create table `index` (
                  `id` int comment '通知排名，越新的通知编号越小',
                  `title` varchar(64),
                  `date` date,
                  `bureau` varchar(8),
                  `link` varchar(128),
                  `details` varchar(16384)
                  );''')
cursor.execute('''create table `appendix` (
                  `fileName` varchar(64),
                  `affiliatedNoticeID` int comment '附件所属的通知ID',
                  `downloadNum` int,
                  `downloadLink` varchar(128)
                  );''')

url = "https://jwch.fzu.edu.cn/jxtz.htm"
index = details = appendix = []
# 教学通知（一级链接）
for i in range(5):
    response = requests.get(url=url).text.encode('ISO-8859-1').decode('utf-8')
    soup1 = bs4.BeautifulSoup(response, 'lxml')

    for j in range(19, 39):
        t1 = soup1.select('li')[j].text
        t1 = t1.replace('\n', '')
        t1 = t1.replace('\r', '')
        t1 = t1.replace(' ', '')
        t2 = t1[11:t1.find('】')]  # 部门
        t1 = t1[0:10]  # 日期
        t3 = soup1.select('li > a')[j - 1]['title']  # 标题
        t4 = "https://jwch.fzu.edu.cn/" + soup1.select('li > a')[j - 1]['href']  # 二级链接
        # print(t1, t2, t3, t4)

        # 【质量办】 关于举办福州大学第四十五场“教学有道”研讨活动的通知 (2023-08-04)
        #  我自行访问上述通知时提示“应用未对接认证服务——您访问的应用尚未接入统一身份认证，请联系相关部门完成对接配置”
        if t4 == 'https://jwch.fzu.edu.cn/../content.jsp?urltype=news.NewsContentUrl&wbtreeid=1040&wbnewsid=12893':
            cursor.execute('insert into `index` values (%s,%s,%s,%s,%s,%s)',
                           (str(i * 20 + j - 18), t3, t1, t2, t4, "该条通知疑似被接入统一认证身份系统，无法抓取该通知。"))
            connection.commit()
            # print("该条通知疑似被接入统一认证身份系统，无法抓取该通知。")
            continue

        response = requests.get(url=t4).text.encode('ISO-8859-1').decode('utf-8')
        soup2 = bs4.BeautifulSoup(response, 'lxml')
        text = soup2.find('div', class_="v_news_content").text.strip('\n')  # 无法处理网页中的表格
        cursor.execute('insert into `index` values (%s,%s,%s,%s,%s,%s);', (str(i * 20 + j - 18), t3, t1, t2, t4, text))
        connection.commit()

        annexName = soup2.select('li > a')  # 附件内可能存在冗余前缀
        annexLink = soup2.select('li > a')
        strDownloadNum = '<li>附件.*?getClickTimes[(](.*?),1744984858,"wbnewsfile","attach"[)]</script></span>次</li>'
        ID = re.findall(strDownloadNum, response, re.S)
        for k in range(len(annexName)):
            param = {'wbnewsid': ID[k],
                     'owner': '1744984858',
                     'type': 'wbnewsfile',
                     'randomid': 'nattach'}
            annexLink[k]['href'] = "https://jwch.fzu.edu.cn" + annexLink[k]['href']  # 补全下载链接
            response2 = requests.get(url='https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp',
                                     params=param)
            annexDownloadNum = response2.json()  # 下载次数
            cursor.execute('insert into `appendix` values (%s,%s,%s,%s)',
                           (annexName[k].text, str(i * 20 + j - 18), annexDownloadNum['wbshowtimes'],
                            annexLink[k]['href']))
            connection.commit()
            # print(annexName[k].text, annexLink[k]['href'], annexDownloadNum['wbshowtimes'])
        print("已导入", i * 20 + j - 18, "/ 100 条")

    if i == 0:
        url = "https://jwch.fzu.edu.cn/" + soup1.select('span > a')[9]['href']
    else:
        url = "https://jwch.fzu.edu.cn/jxtz/" + soup1.select('span > a')[i + 11]['href']

cursor.close()
connection.close()
