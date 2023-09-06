import time
import sys

def get_time():
    local = time.localtime()
    return "{}-{}-{} {}:{}:{}".format(local.tm_year, local.tm_mon, local.tm_mday,
                                      local.tm_hour, local.tm_min, local.tm_sec)

def log(func):
    def debug(*args, **kwargs):
        sys.stderr.write( "\nFunction {} starts running at {}\n".format(func.__name__, get_time()) )
        result = func(*args, **kwargs)
        sys.stderr.write( "\nFunction {} ends running at {}\n".format(func.__name__, get_time()) )
        return result
    return debug

@log
def wait(sec):
    print("wait for {} second{}".format(sec, "s"if(sec!=1)else""))
    time.sleep(sec)


wait(10)