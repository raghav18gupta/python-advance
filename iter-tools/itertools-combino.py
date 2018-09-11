import itertools as it

# product(iter1, iter2)
# cartesian product of the two iterable containers 
print (list(it.product('AB','12'))) 


# permutations(iter, group_size)
# prints all possible permutation of all elements
print (list(it.permutations('abc',1)), end='\n\n') 
print (list(it.permutations('abc',2)), end='\n\n') 
print (list(it.permutations('abc',3)), end='\n\n') 


# combinations(iterable, group_size)
# This iterator prints all the possible combinations(without replacement) of the container passed in arguments in the specified group size in sorted order.
print (list(it.combinations('123',2)), end='\n\n') 



# combinations_with_replacement(iterable, group_size) 
# to print every combination with replacement 
print (list(it.combinations_with_replacement('123',2)), end='\n\n') 


