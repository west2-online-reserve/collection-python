list1 = input()
list2 = list1.split()
list3 = [x for x in list2 if x.isdigit()]
list3 = [int(x) for x in list3]
list3.sort()
print(list3)
