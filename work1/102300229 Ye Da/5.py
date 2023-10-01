import time
def observetime(f):
    def wrapper(*args,**kwargs):
        Start=time.time()
        print("开始时间是",Start)
        a=f(*args,**kwargs)
        End=time.time()
        print("结束时间是",End)
        print("运行时间是",End-Start)
    return wrapper
@observetime
def func(t):
    return time.sleep(t)
t=int(input("你的测试数据是几秒\n"))
func(t)
'''
#进阶版
import time
def observerun(times):
    
    def diaoyonghanshu(func):
        
        def wrapper(*args,**kwargs):
            
            start=time.time()
            for i in range(times):

                b=func(*args,**kwargs)

            end=time.time() 

            print("运行",times,"次","函数",func,"所需的时间为",end-start)

            return b

        return wrapper

    return diaoyonghanshu

n=int(input("你要运行几次函数\n"))

@observerun(n)

def sample(t):

    return time.sleep(t)

t=int(input("你的测试数据是几秒\n"))

sample(t)
'''