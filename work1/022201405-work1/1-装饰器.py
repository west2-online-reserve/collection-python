import time,random
def a(f):
    def b(x):
        timestart = time.time()
        f(x)
        print("开始时间:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'格林-----时间戳',timestart)
        timeend=time.time()
        print("结束时间:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'格林-----时间戳',timeend)
        print("用时：%.30f"%(timeend-timestart))
    return b
@a
def callback(name):
    time.sleep(random.random())
    print("函数名称",name)
if __name__=="__main__":
    callback("callback")
#github:2877378857qq.com   西二--作业