import functools
import time

"""
This is the example how decorator can be useful in case of recursive call,
decorator here define cache and store values in cache, so every recursive call it return cached value
instead of calling function.

"""

#Define Cache decorator that creates cache and remember state
def memorize(function):
    #passed function cache
    function.cache = dict()


    @functools.wraps(function)
    def _mem (*args):
        #check if passed function does not have args then create new one
        if args not in function.cache:
            function.cache[args] = function(*args) # Here actual function call happen
        return function.cache[args] # if cache is exist, then just return value from cache
    return _mem


@memorize
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


def fibo_w(n):
    if n < 2:
        return n
    else:
        return fibo_w(n-1) + fibo_w(n-2)


for i in range(1,40):
    t1 = time.time()
    fibo(i)
    #print('with cache fibo {}: {} '.format(i,fibo(i)))
    t2 = time.time()

print("Execution time with cache: {}".format(t2-t1))

for i in range(1,40):
    t1 = time.time()
    fibo_w(i)
    #print('fibo {}: {} '.format(i,fibo_w(i)))
    t2 = time.time()
print("Execution time without cache: {}".format(t2 - t1))

"""
Execution time with cache: 9.5367431640625e-07
Execution time without cache: 21.78167414665222

Process finished with exit code 0

"""
