list1=[1,2,3,1,1,2]
def func(list1):
    count={}
    for num in list1:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return count
print(func(list1))