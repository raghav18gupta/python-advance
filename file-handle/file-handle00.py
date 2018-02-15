with open('files/txt-file00.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

with open('files/txtfile0.txt', 'r') as rf:
    with open('files/txtfile-copy.txt', 'w') as wf:

        for line in rf:  # copying line by line
            wf.write(line)

# Don't do this, file will be damaged!
'''with open('files/python_file3.png', 'r') as rf:
    with open('files/python_file-copy.png', 'w') as wf:

        for line in rf: #copying line by line
            wf.write(line)
'''

# Open in binary mode
with open('files/python_file3.png', 'rb') as rf:
    with open('files/python_file-copy.png', 'wb') as wf:

        for line in rf:  # copying line by line
            wf.write(line)

with open('files/python_file3.png', 'rb') as rf:
    with open('files/python_file-copy1.png', 'wb') as wf:

        readfile = rf.read(1024)
        while len(readfile) > 0:
            wf.write(readfile)
            readfile = rf.read(1024)
