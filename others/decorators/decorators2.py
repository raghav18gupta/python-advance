def decoratorFUNC(originalFUNC):
    def wrapperFUNC():
        print('wrapperFUNC executed be4 "{}"'.format(originalFUNC.__name__))
        return originalFUNC()   # executes and return
    return wrapperFUNC


@decoratorFUNC
def displayFUNC():
    print('display function')


displayFUNC()

'''
output:
wrapperFUNC executed be4 "displayFUNC"
display function
'''

'''
# Line 7 & 8 is same as:
displayFUNC = decoratorFUNC(displayFUNC)
# it means displayFUNC got new functionality
'''
