import time


def decorator(func):
    def inner(*args, **kwargs):
        print(func.__name__)
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f' begin:{begin},\n end:{end},\n during:{end - begin}')

    return inner

