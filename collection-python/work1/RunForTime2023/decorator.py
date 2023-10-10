import time


def Test(func):
    def Decorator():
        a = time.localtime()
        result = func();
        b = time.localtime()
        print("Start Time:\t\t", time.strftime("%Y/%m/%d %H:%M:%S", a))
        print("End Time:\t\t", time.strftime("%Y/%m/%d %H:%M:%S", b))
        print("Time Interval:\t", time.perf_counter(), "s")
        return result
    return Decorator


@Test
def execute():
    print("Function Name:\t", execute.__name__, "\n")
    time.sleep(3)

execute()