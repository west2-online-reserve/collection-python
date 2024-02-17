import time

def dec(func):
    def display():
        st = time.time()
        print("Function name: {}()".format(func.__name__))
        func()
        ed = time.time()
        print("start: {}\nend: {}\ninterval: {}".format(st, ed, ed - st))
    return display

@dec
def func():
    print("Hello world")

func()