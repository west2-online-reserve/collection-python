# import time
# def decorator(func):
#     def wrapper(*args,**kw):
#         start = time.time()
#         print(f'执行函数: {func.__name__}')
#         result = func(*args,**kw)
#         end = time.time()
#         run = end - start
#         print(f'开始时间：{start}')
#         print(f'结束时间：{end}')
#         print(f'运行时间：{run}')
#         return result
#         
#     return wrapper
# @decorator
# def function():
#     time.sleep(8)
# 
# function()

#突然发现上面返回的时间不大正常，百度后发现表示的是自某个特定时间点（通常是1970年1月1日午夜，称为Unix纪元）以来的秒数，因此，我尝试再次引入函数，把它变成人能看的东西 

import time
import datetime

def decorator(func):
    def wrapper(*args,**kw):
        start = time.time()
        start = datetime.datetime.fromtimestamp(start)
        print(f'开始执行：{func.__name__}')
        result = func(*args,**kw)
        end = time.time()
        end = datetime.datetime.fromtimestamp(end)
        run = end - start
        print(f'开始时间：{start}')
        print(f'结束时间：{end}')
        print(f'运行时间：{run}')
        return result
    return wrapper
@decorator
def function():
    time.sleep(8)
function()

















