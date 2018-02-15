class Open_File(object):

    def __init__(self, filename, mode):  # constructor
        self.filename = filename
        self.mode = mode

    def __enter__(self):  # called, when 'with as' statement runs
        self.file = open(self.filename, self.mode)
        return self.file  # returns to f

    def __exit__(self, exe_type, exc_val, traceback):  # on exiting 'with as'
        pass


with Open_File('files/txtfile-copy.txt', 'w') as f:
    f.write('Testing')

print(f.close)
