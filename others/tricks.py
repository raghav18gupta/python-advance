# comparision
a, b = 1, 2
print((a, b)[a < b])  # a if False else b
print((lambda: a, lambda: b)[a < b]())
print("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")

# any() all()
print(any([]))
print(all([]))
