listA=eval(input())
listB=[x for x in listA if type(x)!=str]
listC=sorted(listB)
print(listC)
