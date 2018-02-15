'''find word from file'''
import re
import argparse


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help='specify word for search for')
    parser.add_argument('fname', help='specify file to search for')
    args = parser.parse_args()

    searchfile = open(args.fname)
    papa = False
    for line in searchfile.readlines():
        searchres = re.search(args.word, line, re.M | re.I)
        if searchres:
            print('Match found ho gaya')
            papa = True
            break
    if not papa:
        print('match nahi ho paaya')


if __name__ == '__main__':
    Main()
