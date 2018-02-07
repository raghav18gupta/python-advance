a = 1,2,3
b = "r_g"
print (zip(a, b))
print zip(*zip(a, b))
# [(1, 'r'), (2, '_'), (3, 'g')]
# [(1, 2, 3), ('r', '_', 'g')]
# [Finished in 0.047s]

#transpose matrix
a = [[0,1,2], [3,4,5], [6,7,8]]
print zip(*a)   # *unpack and zip()
# [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
# [Finished in 0.052s]
