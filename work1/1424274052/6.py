def tj(list1=[]):
    dict1={}
    for i in list1:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    print(dict1)
list1=list(input('请输入一个数字列表：'))
tj(list1)