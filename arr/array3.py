import array

arr1 = array.array('i', [1, 2, 3, 1, 2, 5])
arr2 = array.array('i', [9, 8, 7])

# using count() to count occurrences of 1 in array
print(arr1.count(1))    # 2

# using extend() to add array 2 elements to array 1
arr1.extend(arr2)   # The modified [arr1] : [1, 2, 3, 1, 2, 5, 9, 8, 7]

li = [1, 2, 3]

# using fromlist() to append list at end of array
arr2.fromlist(li)   # arr2 = [9, 8, 7, 1, 2, 3]

# using tolist() to convert array into list
li2 = arr1.tolist() # li = [1, 2, 3, 1, 2, 5, 9, 8, 7]


# arr2.typecode returns 'i'

newarr = array(arr2.typecode, [x for x in arr2])

print(newarr)