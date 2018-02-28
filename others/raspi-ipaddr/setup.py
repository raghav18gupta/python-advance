#!/usr/bin/python3
import subprocess
import os

FNULL = open(os.devnull, 'w')
print('installing\n   -> gTTS\n   -> mpg123')
a = subprocess.Popen('pip3 install gTTS', stdin=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT, stdout=FNULL)
b = subprocess.Popen('sudo apt-get install mpg123 -y', stdin=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT, stdout=FNULL)

while (a.poll() and b.poll()) is None:
    pass

print('setup complete')
