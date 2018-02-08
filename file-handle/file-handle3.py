readfile = open('files/txtfile1.txt', 'r').read()
print(readfile)
# readfile.close()

readfile = open('files/txtfile1.txt', 'r').readlines()
for line in readfile:
    print(line, end="")
