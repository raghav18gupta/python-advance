# https://www.geeksforgeeks.org/iterator-functions-in-python-set-1/
# https://www.youtube.com/watch?v=xK7E2YmjyAc



import itertools as it


def simple_func(a, b):	# Two parameters needed for it.accumulator
	return (a+b)/(a-b)


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


# chain()
# groups together multiple lists into one single iterable
x = []
for i in it.chain(a, b, c):
    x.append(i)
print(x)	# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(list(it.chain(a[5:], c[5:])))	# [5, 6, 7, 8, 9, 'f', 'g', 'h', 'i', 'j']


# chain.from_iterable()
print(list(it.chain.from_iterable( [a[:3], c[:3]] )))	# Similar as chain() but the argument here is a list of lists or any other iterable container.


# accumulate(iter, func=sum)
print(list(it.accumulate(a, simple_func)))
print(list(it.accumulate(a)))	# [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]


# compress(iter, selector)
# selectively picks the values to print from the passed container according to the boolean list
container = 'abcdefghijklm'
selector = [1,0,0,0,0,1,0,0,1,0,0,0,0]
print(list(it.compress(container, selector)))


# dropwhile(func, seq)
# starts printing the characters only after the func. in argument returns false
print (list(it.dropwhile(lambda x : x%2==0, [2, 4, 5, 7, 8, 2]))) 


# filterfalse(func, seq) 
# prints only values that return false for the passed function.
print (list(it.filterfalse(lambda x : x%2==0, [2, 4, 5, 7, 8, 2]))) 
