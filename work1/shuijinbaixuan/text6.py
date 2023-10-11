number={
    1001:'张三',
    1002:'李四',
    1003:'王五',
    1004:'赵六',
    1005:'大傻春'}
for i in list(number):
    if i%2==0:
        del number[i]

print(number)
