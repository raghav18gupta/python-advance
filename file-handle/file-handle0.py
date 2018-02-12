with open('files/txtfile0.txt', 'r') as f:
    print(f)    #<_io.TextIOWrapper name='files/txtfile0.txt' mode='r' encoding='UTF-8'>
    print(f.read())   #inefficient
    print(f.tell())     #173
    f.seek(0)
    print(f.tell())     #0

    print(f.readline(), end='')     #1) this is a test file!
    print(f.readline(), end='\n')     #2) with multiple lines of data...

    print(f.readlines())    #['3) third line\n', '4) fourth line\n', '5) fifth line\n', '6) sixth line\n', '7) seven line\n', '8) eighth line\n', '9) ninth line\n', '10) tenth line\n']
    print()
    f.seek(0)

    print('='*100)
    for line in f:      #print line by line
        print(line, end='')
    print()
    f.seek(0)

    print('+'*100)
    print(f.read(100))  #1) to 5)
    print(f.read(100), end='\n')    #6) to 10)
    print(f.read(100))  #nothing would br printed
    f.seek(0)

    print('-'*100)
    read_content = f.read(10)
    while len(read_content) > 0:
        print(read_content, end='*')
        read_content = f.read(10)


    print(f.name)   #files/txtfile0.txt

print(f.closed)  #True
