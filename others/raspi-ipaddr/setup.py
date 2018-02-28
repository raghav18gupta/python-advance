#!/usr/bin/python3
import subprocess

a = subprocess.Popen('pip3 install gTTS', stdin=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)
while a.poll() !=0:
  pass
subprocess.Popen('sudo apt-get install mpg123 -y', stdin=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)
