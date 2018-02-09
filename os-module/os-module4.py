import os

#to print directory tree
os.chdir('/home/raghav/Desktop/gitHub')
open('x.txt', 'w')
for dirPath, dirName, fileName in os.walk('/home/raghav/Desktop/gitHub'):   #os.walk() is a generator which yeilds 3 tuple
    print('curr path:\t', dirPath)
    print('dir name:\t', dirName)
    print('file name:\t', fileName)
    print()

print(os.environ.get('HOME'))   #/home/raghav
fileName = os.environ.get('HOME') + 'x.txt'     #we want to have x.txt at HOME dir
print(fileName)     #/home/raghavx.txt     but we miss / here

#so we use os.path(), which joins two paths together
fileName = os.path.join(os.environ.get('HOME'), 'x.txt')    #/home/raghav/x.txt
print(fileName)
fileName = os.path.basename('/home/raghav/Desktop/lala.txt')
print(fileName)     #lala.txt
fileName = os.path.dirname('/home/raghav/Desktop/lala.txt')
print(fileName)     #/home/raghav/Desktop
fileName = os.path.split('/home/raghav/Desktop/lala.txt')
print(fileName)     #('/home/raghav/Desktop', 'lala.txt')
fileName = os.path.exists('/home/raghav/Desktop/lala.txt')
print(fileName)     #False, because it is fake path
fileName = os.path.isfile('/home/raghav/Desktop/gitHub/what-I-learned/py-advance/os-module/os-module1.py')
print(fileName)     #True
fileName = os.path.isdir('/home/raghav/Desktop/gitHub/what-I-learned/py-advance/os-module/os-module1.py')
print(fileName)     #False
fileName = os.path.splitext('/home/raghav/Desktop/gitHub/what-I-learned/py-advance/os-module/os-module1.py')
print(fileName)

os.remove('x.txt')
