import requests
import pymysql

print("请输入本机MySQL的root用户密码：", end='')  # 不检查正确性
password = input()
connection = pymysql.connect(host='localhost', user='root', password=password)
cursor = connection.cursor()
cursor.execute('drop database if exists history')
cursor.execute('create database history charset=utf8')
connection = pymysql.connect(host='localhost', user='root', password=password, database='history', charset='utf8')
cursor = connection.cursor()

tempStr = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
           '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1, 13):
    url = 'https://baike.baidu.com/cms/home/eventsOnHistory/' + tempStr[i] + '.json'
    response = requests.get(url=url).json()
    for j in range(1, date[i] + 1):
        cursor.execute('''create table `%s月%s日` (
                          `year` varchar(8),
                          `eventKind` varchar(8),
                          `title` varchar(32),
                          `desc` varchar(512)
                          );''', (i, j))
        print("正在将", i, "月", j, "日的数据写入SQL")
        tempList = response[tempStr[i]][tempStr[i] + tempStr[j]]
        for k in range(len(tempList)):
            title, description = tempList[k]['title'], tempList[k]['desc']
            title = title.replace(' ', '')
            title = title.replace('\n', '')
            title2 = title.replace(title[title.find('<'):title.find('>') + 1], '')
            title2 = title2.replace('</a>', '')
            while (title != title2):
                title = title2
                title2 = title2.replace(title2[title2.find('<'):title2.find('>') + 1], '')

            description += '...'
            description = description.replace('\n', '')
            desc = description.replace(description[description.find('<'):description.find('>') + 1], '')
            desc = desc.replace('</a>', '')
            desc = desc.replace(desc[desc.find('['):desc.find(']') + 1], '')
            desc = desc.replace('&nbsp', '')
            while (description != desc):
                description = desc
                desc = desc.replace(desc[desc.find('<'):desc.find('>') + 1], '')
                desc = desc.replace(desc[desc.find('['):desc.find(']') + 1], '')
            cursor.execute('insert into `%s月%s日` values (%s,%s,%s,%s)',
                           (i, j, tempList[k]['year'], tempList[k]['type'], title, description))

cursor.close()
connection.close()
