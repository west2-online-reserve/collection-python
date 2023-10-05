import time

def count_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret = func(*args, **kwargs)
        t2 = time.time()
        t3 = t2 - t1
        name1 = func.__name__
        print("执行的函数名称为：",name1)
        print("开始执行的时间为:",'{:.2f}'.format(t1))
        print("执行的时间为：",'{:.2f}'.format(t3))
        print("结束执行的时间为：", '{:.2f}'.format(t2))
        return ret

    return wrapper


@count_time
def func1_for_test(x):
    time.sleep(x)


if __name__ == '__main__':
    func1_for_test(2)
