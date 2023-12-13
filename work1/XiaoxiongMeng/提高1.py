import time
from random import randint


def time_dec(f):
    def s(n):
        t1 = time.time()
        print(f.__name__)
        f(n)
        time.sleep(0.001)
        t2 = time.time()
        print(f"运行共用时{t2 - t1}秒")

    return s


@time_dec
def cat(n):
    i = 0
    print(f"现在是1号,猫哥现在有{n}元生活费")
    while n != 0 and i <= 30:
        s = randint(1, min(50,n))
        n = n - s
        i += 1
        print(f"猫哥贪吃买了点小零食,花掉了{s}元,现在是{i}号,还有{n}元生活费")
    if n == 0:
        print(f"今天是{i}号,猫哥现在没有钱了,又要被迫减肥了")
    else:
        print(f"猫哥这个月还剩下{n}元")


a = int(input("今天是1号,猫哥需要一些生活费,请你酌情给他一些生活费"))
cat(a)
