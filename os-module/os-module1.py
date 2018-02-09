import os

pwd = os.getcwd()
print(pwd)  #/home/raghav/Desktop/gitHub/what-I-learned/py-advance/os-module

os.mkdir('newDIR')
print('newDIR directory created')


import time


time.sleep(2)
os.rename('newDIR', 'newDir')
print('newDIR renamed to newDir')

time.sleep(2)
os.rmdir('newDir')
print('newDir removed')
