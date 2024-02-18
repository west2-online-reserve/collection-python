import pandas as pd
import pymysql
#from scipy.stats import chi2_contingency
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='fzu_notice')
sql = "SELECT AUTHOR,DOWNLOAD_NUM FROM FILES;"
data=pd.read_sql(sql,conn)
result = data.groupby('AUTHOR')['DOWNLOAD_NUM'].sum()
print(result)
sql = "SELECT TIME FROM NOTICE;"
data1=pd.read_sql(sql,conn)
print(data1['TIME'].value_counts())
