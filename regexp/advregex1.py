import re


def Main():
    line = 'I think i understand regular language'

    matchres = re.match('think', line, re.M | re.I)
    if matchres:
        print("Match found", matchres.group())
    else:
        print("No match found in match")

    searchres = re.search('think', line, re.M | re.I)
    if searchres:
        print("Match found", searchres.group())
    else:
        print("No match found in search")


if __name__ == '__main__':
    Main()
