def f(lists) :
    dict={}
    for i in lists :
        a=lists.count(i)
        dict[f"{i}的个数"]=a
    print(dict)
