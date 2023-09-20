def count(list):
    dict={}
    n=len(list)
    for i in range(n):
        if list[i] in dict :
            dict[list[i]]+=1
        else:
            dict[list[i]]=1
    return dict
print(count([1,2,2,24,34,34]))