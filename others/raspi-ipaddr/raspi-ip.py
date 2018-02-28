#!/usr/bin/python3
from gtts import gTTS
import subprocess
import os

FNULL = open(os.devnull, 'w')
IPAddr = subprocess.check_output("ip route get 8.8.8.8 | awk '{print $NF; exit}'", stdin=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT).decode('UTF-8').rstrip().split('.')

txt = 'IP address of your device is{0}dot{1}dot{2}dot{3}'.format(*IPAddr)
language = 'en'

ttsobj = gTTS(text=txt, lang=language, slow=False)
ttsobj.save('IPAddr.mp3')

while True:
    say = subprocess.Popen('mpg123 IPAddr.mp3', stdin=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT, stdout=FNULL)
    while say.poll() != 0:
        pass
