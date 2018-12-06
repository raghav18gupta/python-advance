import array

arr = array.array('i', [10, 20, 40, 30, 40, 50, 40])

# insertion:
arr.insert(1, 60)   # arr = [10, 60, 20, 40, 30, 40, 50, 40]

# count occurance of 40:
print(arr.count(40))    # prints 3

# deletion - delete only one 40:
arr.remove(40)      # arr = [10, 60, 20, 30, 40, 50, 40]

# practicle deletion:
while arr.count(40):    # arr = [10, 60, 20, 30, 50]
    arr.remove(40)

# find 'index' of element
print(arr.index(20))    # prints 2

