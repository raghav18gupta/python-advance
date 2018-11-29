from array import array

# array(data type, value list)
a = array('i', [2, 3, 4, 5, 5, 5, 6, 1])

print(a)
for i in a:
    print(i)

a.append(1211)
print(a)
a.insert(23423, 2)  # index
print(a)

try:
    a.append("assss")
except:
    pass

print(a)  # no change

'''index() , remove() can be applied, as in list'''
'''
http://www.geeksforgeeks.org/array-in-python-set-2-important-functions/

'''
