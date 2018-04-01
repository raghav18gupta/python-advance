# comparision
a, b = 1, 2
print((a, b)[a < b])  # a if False else b
print((lambda: a, lambda: b)[a < b]())
print("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")

# any() all()
print(any([]))
print(all([]))

#prime and nonprime using list comprehension
nonprime = [j for i in range(2, 8) for j in range(i*2, 50, i)]
prime = [x for x in range(2, 50) if x not in nonprime]
#a efficient way
prime = [x for x in range(2, 50) if all(x % y != 0 for y in range(2, int(x**0.5 + 1)))]
print(prime)