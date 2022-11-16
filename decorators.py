

import math
import time


def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)

        func(*args,**kwargs)

        finish=time.time()
        print(f"fonksiyon {func.__name__} {start-finish} saniye sürdü.")
    return inner


@calculate_time
def usAlma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))


@calculate_time
def toplama(a,b):
    print(a+b)


toplama(5,5)
usAlma(2,3)
faktoriyel(4)


