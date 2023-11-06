# 实现一个装饰器，在开始执行函数时输出该函数名称， 并在结束时输出函数的开始时间和结束时间以及运行时间
import time
import datetime


def func_execute_time(iteration):
    def inner(func):
        def wrapper(*args, **kwargs):
            global result
            start = time.perf_counter()
            print(f"begin time: {datetime.datetime.now()}")
            for i in range(iteration):
                result = func(*args, **kwargs)
            print(f"end time: {datetime.datetime.now()}")
            print(f"{func.__name__} execute time: {time.perf_counter() - start:.7f}s")
            return result

        return wrapper

    return inner


@func_execute_time(1)
def power(x, n):
    time.sleep(1)
    return x * n


print(power(7, 2))
