import time
import functools
import sys
sys.setrecursionlimit(65535)
"""
This example shows efficient way of using caching 
"""

def cache(function):
    function.cache = dict()

    @functools.wraps(function)
    def _cache(*args):
        if args not  in function.cache:
            function.cache[args] = function(*args)

        return function.cache[args]
    return _cache

@cache
def factorial_cached(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_cached(n-1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

t1 = time.time()
for i in range(10000):
    factorial_cached(i)
    #print("Factorial {} with cache is {}".format(i, factorial_cached(i)))
t2 = time.time()
print("Cached Factorial time for calculate 10000! is {} Seconds".format(t2-t1))

t3 = time.time()
for i in range(10000):
    factorial(i)
    #print("Factorial {} without cache is {}".format(i, factorial(i)))
t4 = time.time()

print("Normal Factorial time for calculate 10000! is {} Seconds ".format(t4-t3))

"""
Cached Factorial time for calculate 10000! is 0.05981731414794922 Seconds
Normal Factorial time for calculate 10000! is 129.45578908920288 Seconds 

"""
