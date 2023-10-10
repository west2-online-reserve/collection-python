import datetime
import time


def counttime_and_printname(func):
    def wrapper():
        start_time = datetime.datetime.now()
        print("开始时间是：",start_time)
        print("函数名称是：",func.__name__)
        func()
        end_time = datetime.datetime.now()
        print("结束时间是：",end_time)
        print("运行时间是：",(end_time - start_time).total_seconds(),"秒")
    return wrapper

@counttime_and_printname
def function1():
    time.sleep(2)


function1()