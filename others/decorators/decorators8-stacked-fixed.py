from functools import wraps


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='logs/{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper


@my_logger
@my_timer
def simpleFUNC(a):
    import time
    time.sleep(2)
    print(a)


simpleFUNC('fixed decorator using functool')

simpleFUNC = my_timer(simpleFUNC)
print(simpleFUNC.__name__)  # prints 'simpleFUNC'


'''
It's 1:43 a.m.. Time to commit :')
'''
