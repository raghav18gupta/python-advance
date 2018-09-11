# https://www.geeksforgeeks.org/iterator-functions-python-set-2islice-starmap-tee/

import itertools as it

li = [2, 4, 5, 7, 8, 10, 20] 
t_list = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10 , 1) ] 


# islice(iterable, start, stop, step)
# selectively prints the values mentioned in its iterable container
print (list(it.islice(li, 1, 6, 2)))


# starmap(func., tuple list)
# returns the value according to the function from each tuple of list.
print (list(it.starmap(max,t_list)))


# takewhile(func, iterable)
# opposite of dropwhile(), it prints the values till the function returns false for 1st time.
print (list(it.takewhile(lambda x : x%2==0,li ))) 


# tee(iterator, count)
# splits the container into a number of iterators mentioned in the argument.
itr_li = iter(li)
tee_li = it.tee(itr_li, 3)		# Here "li" can also be used insted of "itr_li"
for i in tee_li:
	print (list(i))


# zip_longest( iterable1, iterable2, fillval.) 
# prints the values of iterables alternatively in sequence. If one of the iterables is printed fully, remaining values are filled by the values assigned to fillvalue.
print (list(it.zip_longest('loonngg','short',fillvalue='-' ))) 

