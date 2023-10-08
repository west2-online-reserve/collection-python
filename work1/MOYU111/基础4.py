list1 =[1,5,7,3,5,'123','154','111']
for i in range(1,len(list1)):
    if type(list[i]) == str:
        del list[i]
        i=i-1
list1=list1.sorted()
print(list1)