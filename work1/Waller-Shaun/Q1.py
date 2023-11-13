from functools import wraps
import time
def decorator(fun):
    @wraps(fun)
    def wrap_the_function():
        print(fun.__name__)
        T1 = time.perf_counter()
        fun()
        T2 = time.perf_counter()
        during_time = T2-T1
        print('Starting time: %f \nEnding time: %f \nDuring time: %f(s)'%(T1,T2,during_time))
    return wrap_the_function

@decorator
def funtion_need_to_be_decorated():
    for i in range(100*100):
        pass

funtion_need_to_be_decorated()


import os
print(os.getcwd())