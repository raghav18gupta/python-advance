from collections import defaultdict

############## example - 1 ##############

d = defaultdict(lambda : 'default')  # argument must be callable or None

d['a'] = 1
d['b'] = 2

print(d)    # defaultdict(<function <lambda> at 0x7fd7c23901e0>, {'a': 1, 'b': 2})

print(d['c'])   # default

############## example - 2 ##############

colours = (
    ('Yasoob', 1),
    ('Ali', 2),
    ('Arham', 3),
    ('Ali', 4),
    ('Yasoob', 7),
    ('Ahmed', 4),
)

d = defaultdict(list)

for k, v in colours:
    d[k].append(v)

print(d)    # defaultdict(<class 'list'>, {'Yasoob': [1, 7], 'Ali': [2, 4], 'Arham': [3], 'Ahmed': [4]})

############## example - 3 ##############

d = defaultdict(int)

for i in 'mississippi':
    d[i]+=1

print(d)    # defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})
