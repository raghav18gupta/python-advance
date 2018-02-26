import subprocess

try:
    end = subprocess.check_output(['python3', 'bad-script/bad-script.py'], stderr=subprocess.STDOUT, timeout=2)
except subprocess.TimeoutExpired as e:
    end = 'Error: exection time more then 2 seconds'

print(end)
