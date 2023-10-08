listA=[123,122,133,2266,236,122,111]
def func(listA):
    count={}
    for i in listA:
        count[i]=0
    for i in listA:
        count[i]+=1
    return count
print(func(listA))
