import time
def c_time(f):
    def inner ():
        print('函数名：',f.__name__)
        start_time=time.time()
        f()
        end_time=time.time()
        print('开始时间：',start_time)
        print('结束时间：',end_time)
        print('运行时间：',end_time-start_time)
    return inner
@c_time
def hello():
    time.sleep(2)
    print('hello world!')
hello()