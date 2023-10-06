list=['happy',5,9,"fzu",13]

for i in list:
    if type(i) == str :
        list.remove(i)

list.sort()
print(list)