import time


def time_decorator(func):  # 装饰器本身是一个函数，它接受一个函数作为参数，并返回一个新的函数。
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"开始执行函数：{func.__name__}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"开始时间：{start_time}")
        print(f"结束时间：{end_time}")
        print(f"运行时间：{end_time - start_time}秒")
        return result

    return wrapper


@time_decorator  # 调用 example_function() 时，实际上你调用的是 time_decorator(example_function)。
def example_function():
    print("这是一个示例函数：")
    time.sleep(2)


if __name__ == "__main__":
    example_function()
