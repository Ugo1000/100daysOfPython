from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        time1 = time()
        result = func(*args, **kwargs)
        time2 = time()
        print(f'it took {time2 - time1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000):
        i * 5


long_time()
