class decorator_class:

    def __init__(self, originalFUNC):
        self.originalFUNC = originalFUNC

    def __call__(self, *args, **kwargs):
        print('__call__ executed be4 "{}"'.format(self.originalFUNC.__name__))
        return self.originalFUNC(*args, **kwargs)   # executes and return


@decorator_class
def displayFUNC():
    print('display function')


@decorator_class
def displayINFO(name, age):
    print('{} is {} years old'.format(name, age))


displayFUNC()
displayINFO('raghav', 3000)
