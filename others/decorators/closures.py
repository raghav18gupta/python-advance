'''
A closures is an inner function that remembers
and has access to variables in local scope in
which it was created, even after outer function
has finished executing. First Class Functions are
just the concept that functions can be used like
any other objects in your code. Closures use first
class functions in a specific manner.﻿
'''


##############################
def outer():
    msg = 'Raghav Gupta'

    def inner():
        print(msg)

    return inner()  # exexuted here


f = outer()     # Raghav Gupta
print(f)    # None


##############################
def outerFUNC():
    msg = 'Raghav Gupta'

    def innerFUNC():
        print(msg)

    return innerFUNC  # not exexuted here


outerFUNC()()   # Raghav Gupta
f = outerFUNC()
print(f)    # <function outerFUNC.<locals>.innerFUNC at 0x7fb3c4f6aae8>
f()     # Raghav Gupta


##############################
def outerNEW(message):
    msg = message

    def innerNEW():
        print(msg)

    return innerNEW  # not exexuted here


f = outerNEW('Raghav')
f()     # Raghav
