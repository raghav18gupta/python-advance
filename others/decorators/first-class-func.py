
''' A programming language is said to have first-class functions
 if it treats functions as first-class citizens. This means
 the language supports passing functions as arguments to other
 functions, returning them as the values from other functions,
 and assigning them to variables or storing them in data structures.    '''

##############################


def square(x):
    return x ** 2


f = square(4)
print(f)    # 16

f = square
print(f)    # <function square at 0x7f6e91590e18>


##############################
def my_map(func, arguments):
    result = []
    for i in arguments:
        result.append(func(i))
    return result


f = my_map(square, [1, 2, 3, 4, 5])
print(f)    # [1, 4, 9, 16, 25]


##############################
def logger(msg):

    def logmsg():
        print('Log: ', msg)

    return logmsg


f = logger('Raghav Gupta')
print('@@@@')
f()
'''Output:
@@@@
Log:  Raghav Gupta
'''


##############################
def html(tag):

    def wrap_text(msg):
        print('<{0}>{1}<{0}>'.format(tag, msg))

    return wrap_text


h1 = html('h1')
h1('Heading H1')    # <h1>Heading H1<h1>

p = html('p')
p('this is a paragraph!')   # <p>this is a paragraph!<p>
