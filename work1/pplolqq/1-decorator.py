# p1
def encslat(temp):#封装
    import time
    def els():
     begin = time.perf_counter()
     temp()
     end = time.perf_counter()
     print(begin)
     print(end)
     print(end-begin)
    return els
@encslat
def func():
    print(111)
func()