import numpy
import pandas
import pymysql
import matplotlib.pyplot as plt

# print("请输入本机MySQL的root用户密码：", end='')  # 不检查正确性
# password = input()
password = '124578Ch!'
connection = pymysql.connect(host='localhost', user='root', password=password, database='notices', charset='utf8')
cursor = connection.cursor()

cursor.execute('select `affiliatedNoticeID`,`downloadNum` from `appendix`')
annexList = list(cursor.fetchall())
for i in range(len(annexList)):
    annexList[i] = list(annexList[i])
    cursor.execute('select `bureau` from `index` where `id`=%s', annexList[i][0])
    annexList[i].append(cursor.fetchone()[0])
dataFrame = pandas.DataFrame(data=annexList, columns=['id', 'downloadNum', 'bureau'])
dataFrame = dataFrame.groupby('bureau').sum()
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams["axes.unicode_minus"] = False
dataFrame['downloadNum'].plot()
plt.show()

cursor.execute('select `date` from `index`')
dateList = numpy.array(cursor.fetchall())
dateList = zip(dateList.take(0, axis=1), numpy.ones(100, dtype='int32'))
dataFrame = pandas.DataFrame(data=dateList, columns=['date', 'total'])
dataFrame = dataFrame.groupby('date').sum().sort_values(by='total', ascending=False)
dataFrame.to_csv("单日通知数排序.csv")
cursor.close()
connection.close()
