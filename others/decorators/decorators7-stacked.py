def my_timer(orig_func):
    import time

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


simpleFUNC('helo world')
# problem here is wrapper.log is created insted of simpleFUNC.log
# so we fix with functool module (to preserve the information of orig_func)


simpleFUNC = my_timer(simpleFUNC)
print(simpleFUNC.__name__)  # prints 'wrapper'
# simpleFUNC = my_logger(my_timer(simpleFUNC))
