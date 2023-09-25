# -*- coding: utf-8 -*-
def dict1(dict):
    dict2={}
    for x in dict :
        if isinstance(x,int) and x%2==0:
            dict2[x]=dict[x]
        else :
            continue
    return dict2
n=int(input('打算输入几个学号：'))
dict={}
for i in range(n):
    xh=int(input('请输入学号:'))
    xm=str(input('请输入姓名:'))
    dict[xh]=xm
print(dict1(dict))



    







 







