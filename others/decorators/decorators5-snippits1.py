# A snippit decorator function
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='logs/{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper


@my_logger
def simpleFUNC():
    print('Hello world')


@my_logger
def simpleFUNC2(a, b, *args):
    print(a, b, args)


simpleFUNC()
simpleFUNC2('raghav', 'gupta', 1, 2, 3, 4, 5, 6)
