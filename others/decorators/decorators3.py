def decoratorFUNC(originalFUNC):
    def wrapperFUNC(*args, **kwargs):
        print('wrapperFUNC executed be4 "{}"'.format(originalFUNC.__name__))
        return originalFUNC(*args, **kwargs)   # executes and return
    return wrapperFUNC


@decoratorFUNC
def displayFUNC():
    print('display function')


@decoratorFUNC
def displayINFO(name, age):
    print('{} is {} years old'.format(name, age))


displayFUNC()
displayINFO('raghav', 3000)
