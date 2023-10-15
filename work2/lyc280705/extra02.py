import pandas as pd
import pymysql
from scipy.stats import chi2_contingency
conn = pymysql.connect(host='localhost', port=3306, user='root', password='lyc050728', database='fzu_notice')
sql = "SELECT attach_times,section FROM notice;"
data=pd.read_sql(sql,conn)
print(data)
cross_tab = pd.crosstab(data['attach_times'], data['section'])
print(cross_tab)
chi2, p, dof, expected = chi2_contingency(cross_tab)
print("chi2:", chi2)
print("p-value:", p)
sql2="SELECT time FROM notice;"
data2=pd.read_sql(sql2,conn)
grouped_data = data2.groupby('time').size().reset_index(name='count')
sorted_data = grouped_data.sort_values(by='count', ascending=False)
print(sorted_data)