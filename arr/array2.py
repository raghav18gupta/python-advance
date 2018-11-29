import array

arr= array.array('i',[1, 2, 3, 1, 5])
print(arr)

# using pop() to remove element at 2nd position
print(arr.pop(2))
print(arr)

# using remove() to remove 1st occurrence of 1
arr.remove(1)
print(arr)


arr= array.array('i',[1, 2, 3, 1, 2, 5])
# using index() to print index of 1st occurrenece of 2
print("The index of 1st occurrence of 2 is : ", arr.index(2))

# using reverse() to reverse the array
arr.reverse()
print(arr)