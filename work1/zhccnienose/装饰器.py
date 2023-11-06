import functools
import time
import datetime

def tim(func):
    functools.wraps(func)
    
    def inner(*args,**kargs):
        print(func.__name__)    #函数名称
        sttime = datetime.datetime.now()
        res = func(*args,**kargs)
        edtime =  datetime.datetime.now()
        print("开始时间：",sttime)
        print("结束时间：",edtime)
        print("运行时间：",float((edtime-sttime).seconds)) 
        return res
    return inner

@tim
def f(a,b):
    c = a + b
    return c

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f(a,b))