#
def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


@my_timer
def simpleFUNC(a):
    import time
    time.sleep(1)
    print(a)


simpleFUNC('hello world')
# hello world
# simpleFUNC ran in: 1.0012145042419434 sec
