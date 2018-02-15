import threading
import time


class Async(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, 'a')
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print('Finished writing ' + self.out)


def Main():
    message = input('Enter a string to save')
    background = Async(message, 'out.txt')
    background.start()

    print('The program can continue ')
    print('100 + 200 = ',  100+200)

    background.join()
    print('waited for join ')


if __name__ == '__main__':
    Main()
