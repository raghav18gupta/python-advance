from collections import Counter

Counter('mississippi')  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

c = Counter([1, 5, 1, 1, 6, 1])    # Counter({1: 4, 5: 1, 6: 1})

# Counter.elements()
c.elements()    # returns iterator: [1, 1, 1, 1, 5, 6]

# Counter.most_commen()
c.most_common(2)    # returns list: [(1, 4), (5, 1)]



