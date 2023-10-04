'''
1.
实现一个装饰器，在开始执行函数时输出该函数名称， 并在结束时输出函数的开始时间和结束时间以及运行时间
'''


def TimeDc(f):
    import time as T
    def func():
        # 输出函数名
        print(f.__name__)
        #记录函数执行开始的时间戳
        begin=T.time()
        #执行函数
        f()
        #记录函数执行结束的时间戳
        end=T.time()

        BeginTime = T.strftime("开始时间：%H:%M:%S 20%y/%m/%d", T.localtime(begin))
        EndTime = T.strftime("结束时间：%H:%M:%S 20%y/%m/%d",T.localtime(end))

        print(BeginTime)
        print(EndTime)
        print("持续时间：{:f}s".format(end-begin))

    return func

#测试1
@TimeDc
def Text_1():
    pass

#测试2
import time
@TimeDc
def Text_2():
    time.sleep(1)


if __name__=='__main__':
    Text_1()
    Text_2()