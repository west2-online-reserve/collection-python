import pymysql
import pandas as pd
import matplotlib.pyplot as plt

conn = pymysql.connect(host='localhost', user='root', password='3d1415926', database='mydb')
cursor = conn.cursor()
sql = 'SELECT NOTIFER,TIME ,ANNEX_NUMBER FROM FZUDB WHERE ANNEX_NUMBER IS NOT NULL;'
cursor.execute(sql)
result = cursor.fetchall()
cursor.close()
conn.close()

df1 = pd.DataFrame(result, columns=['notify', 'time', 'number'])
df2 = df1.groupby('notify').number.mean().round(0).sort_values(ascending=False)
df3 = df1.groupby('notify').number.sum().sort_values(ascending=False)
df4=df1.groupby('time').number.count()
print('\n平均:',df2,'\n总和:',df3)
df4.plot()
plt.show()
