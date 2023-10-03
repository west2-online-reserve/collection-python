import time
def Test():
    def Decorator():
        a=time.localtime()
        print("Function Name:",Decorator.__name__,"\n")
        time.sleep(3)
        b=time.localtime()
        print("Start Time:",time.strftime("%Y/%m/%d %H:%M:%S",a))
        print("End Time:", time.strftime("%Y/%m/%d %H:%M:%S",b))
        print("Time Interval:",time.perf_counter(),"s")
    return Decorator

t=Test();
t();