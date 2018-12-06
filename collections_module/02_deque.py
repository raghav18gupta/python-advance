from collections import deque

d = deque([0, 1])

# append()
d.append(2)
d.append(3)

# appendleft()
d.appendleft(4)     # deque([4, 0, 1, 2, 3])
d.appendleft(1)
d.appendleft(1)     # deque([1, 1, 4, 0, 1, 2, 3])

# count()
d.count(1)  # returns 3

# clear()
d.clear()   # deque([])

d = deque([0, 1])

# extend()
d.extend([10, 20])  # deque([0, 1, 10, 20)
d.extend(range(30, 50, 10))     # deque([0, 1, 10, 20, 30, 40])

d = deque([0, 1])

# extendleft()
d.extendleft(range(3,5))    # deque([4, 3, 0, 1])

# pop()
d.pop() # returns 1
print(d)    # deque([4, 3, 0])

# popleft()
d.popleft() # returns 4
print(d)    # deque([3, 0])

d = deque([0, 1, 2, 1, 3, 1])

# remove() - removes first occurance of number
d.remove(1) # deque([0, 2, 1, 3, 1])
