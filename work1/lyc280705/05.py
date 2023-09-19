dic={1:'张三',2:'李四',3:'王五',4:'赵六'}
for num in list(dic):
    if num % 2 == 0:
        del dic[num]
print(dic)