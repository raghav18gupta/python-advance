import sys

sys.stderr.write('This is stderr text\n')
# sys.stderr.flush()
sys.stdout.write('This is stderr text\n')

print(sys.argv)
# ~$ python3 sys-module1.py  #['sys-module1.py']
# ~$ python3 sys-module1.py papa  #['sys-module1.py', 'papa']
# ~$ python3 sys-module1.py papa look at that  #['sys-module1.py', 'papa', 'look', 'at', 'that']
# ~$ python3 sys-module1.py papa 'look at that'  #['sys-module1.py', 'papa', 'look at that']
if len(sys.argv) > 1:
    print(sys.argv[1])


#good night
