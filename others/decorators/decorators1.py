'''
Decorator is a function that takes another
function as a argument, add some functionality
to it and then returns another function, without
altering the source code of original function.
'''


def decoratorFUNC(originalFUNC):
    def wrapperFUNC():
        print('wrapperFUNC executed be4 "{}"'.format(originalFUNC.__name__))
        return originalFUNC()   # executes and return
    return wrapperFUNC


def displayFUNC():
    print('display function')


f = decoratorFUNC(displayFUNC)
f()     # prints 'display function'

'''
output:
wrapperFUNC executed be4 "displayFUNC"
display function
'''
