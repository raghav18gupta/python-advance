import itertools as it


# count(start, step)
# This iterator starts printing from the “start” number and prints infinitely. If steps are mentioned, the numbers are skipped else step is 1 by default.
a = it.count(5,2)  # prints -- 5,7,9,11...infinitely


# cycle(iterable)
# This iterator prints all values in order from the passed container. It restarts printing from beginning again when all elements are printed in a cyclic manner.
b = it.cycle([1,2,3,4])  # prints -- 1,2,3,4,1,2,3,4,1...infinitely

# repeat(val, num)
# This iterator repeatedly prints the passed value infinite number of times. If num. is mentioned, them till that number.
c = it.repeat(6,4)  # prints [6, 6, 6, 6]
d = it.repeat(2)



###################################################
# Example #
###################################################
print (list(it.islice(a, 0, 10, 1)), end = '\n\n')
print (list(it.islice(b, 0, 10, 1)), end = '\n\n')
print (list(it.islice(c, 0, 10, 1)), end = '\n\n')
print (list(it.islice(d, 0, 10, 1)), end = '\n\n')