import time

def log_time(func):
    def wrapper(*args, **kwargs):
        print(f"Start  {func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"End  {func.__name__}")
        print(f"Start time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
        print(f"End time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
        print(f"Running time: {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@log_time
def test_function():
    time.sleep(10)

test_function()
