import threading
import time


def Timer(name, delay, repeate):
    print('Timer: ' + name + 'Started')

    while repeate > 0:
        time.sleep(delay)
        print(name + ': ' + str(time.ctime(time.time())))
        repeate -= 1
    print('Timer : ' + name + ' compleated')


def Main():
    t1 = threading.Thread(target=Timer, args=('1', 1, 5))
    t2 = threading.Thread(target=Timer, args=('2', 2, 5))

    t1.start()
    t2.start()

    print('main compleated')


if __name__ == '__main__':
    Main()
