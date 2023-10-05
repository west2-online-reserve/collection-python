def CountNum(l1):
    result1 = []
    result = {}
    for i in l1:
        if i not in result1:
            result[i] = l1.count(i)
    return(result)


yourlist = eval(input('输入一个只有数字的列表'))
print(CountNum(yourlist))
