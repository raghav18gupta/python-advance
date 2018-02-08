'''
CSV = 'comma seprate variable'
with open('filename', 'mode') as f:
    aabrakadabra
# this is done to ensure close of file, even exception caught!
# csv.Dictwriter() and csv.Dictreader()
'''

import csv

with open('files/csvfile.csv', 'r') as csvFile:

    #reader()
    readcsv = csv.reader(csvFile)
    # print(readcsv)  #<_csv.reader object at 0x7f0c797600b8>
    # for row in readcsv:
    #     print(row)
    #      pass

    #writer()
    with open('files/csvfile2.csv', 'w') as csvFile2:
        writercsv = csv.writer(csvFile2, delimiter='|')
        for row in readcsv:
            writercsv.writerow(row)
