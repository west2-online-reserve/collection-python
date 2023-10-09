dic={10001:'张三',10002:'李四',10003:'王五',10004:'赵六'}
for num in list(dic):
    if num % 2 == 0:
        del dic[num]
print(dic)