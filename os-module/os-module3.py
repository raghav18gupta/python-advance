import os
import time

#rename directories
os.mkdir('papa')
time.sleep(2)
os.rename('papa', 'mummy')
time.sleep(2)
os.rmdir('mummy')

#rename files and write file
obj = os.open('x.txt', os.O_RDWR | os.O_CREAT)   # obj = open('x.txt', 'a').close()  #create file 'x.txt'
print(obj)
time.sleep(2)
os.rename('x.txt', 'y.txt')
time.sleep(2)
words = os.write(obj, b'This is the string to be written\n')  #b'aabraacaadaabraa' because TypeError: a bytes-like object is required, not 'str'
os.write(obj, b'Then and now\n')
# print(os.stat('y.txt'))     #os.stat_result(st_mode=33261, st_ino=1186432, st_dev=2055, st_nlink=1, st_uid=1000, st_gid=1000, st_size=46, st_atime=1518194291, st_mtime=1518194291, st_ctime=1518194291)
print(os.stat('y.txt').st_size)  #46 (Bytes)
print('content of file y.txt is \n',open('y.txt', 'r').read())  #content of file y.txt is\nThis is the string to be written\nThen and now\n

os.remove('y.txt')
