'''试用numpy、pandas等库分析初学者作业第一题中：(对人工智能感兴趣的同学尽可能尝试) 要求:

附件下载次数与通知人是否关系，若有，有什么联系？
统计每天的通知数，分析哪段时间通知比较密集？
作业提交请附上报告(代码运行结果及其分析)'''

import pandas as pd
from pymysql import connect
from matplotlib import pyplot as plt

con = connect(host='127.0.0.1', port=3306, user='root', password='root', charset='utf8',database="xing")
page=pd.read_sql("SELECT * FROM files",con=con)

df=pd.DataFrame(page)

#按部门分组，并计算总的文件下载数
data1=df.groupby("agency")["download_num"].sum()
print(data1)

#按日期分组，并计算总的文件下载数
data2=df.groupby("time")["download_num"].sum()
print(data2)

#按时间分组，并计算每天发布附件数
data3=df["time"].value_counts()
print(data3)

#以各个日期为横坐标，以每天文件下载总次数为纵坐标绘制折线图(看错题目额外做的)
data2.plot()
plt.xticks(rotation='vertical')
plt.show()
