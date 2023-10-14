def function(numbers):
    dic={}
    for times in numbers:
        if times in dic:
            dic[times]=dic[times]+1
        else:
            dic[times]=1
    return dic