import os
import time

print(os.getcwd())  #/home/raghav/Desktop/gitHub/what-I-learned/py-advance/os-module
os.chdir('/home/raghav/Desktop/gitHub/')
print(os.getcwd())  #/home/raghav/Desktop/gitHub

print(os.listdir()) #['aast_chang', 'ide', 'what-I-learned']
print(os.listdir('/home/raghav/Desktop/gitHub/what-I-learned/py-advance/'))     #['module', '.git', 'arr', 'others', 'regexp', 'soCkets', 'os-module', 'py-game', 'graph', 'thread--', 'arg-parse', 'file-handle', 'template']

#now
os.chdir('/home/raghav/Desktop/gitHub/what-I-learned/py-advance/os-module')
# os.mkdir('papa1/baccha1')     #error
os.makedirs('papa1/baccha1')
print('papa1/baccha1 created')
time.sleep(2)
os.rmdir('papa1/baccha1')
print('baccha1 removed')
time.sleep(2)
os.rmdir('papa1')
print('papa1 removed')
time.sleep(2)
#again
os.makedirs('papa1/baccha1')
print('papa1/baccha1 created')
time.sleep(2)
os.removedirs('papa1/baccha1')
print('papa1/baccha1 removed')
time.sleep(2)
