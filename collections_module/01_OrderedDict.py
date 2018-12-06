from collections import OrderedDict

'''
    Normal dict can keep track of order of insertion
    of values since python3.6
    OrderedDict is no useful now =)
'''

ordinary_dik = {}
ordinary_dik['Name'] = 'Raghav'
ordinary_dik['Age'] = 21
ordinary_dik['height'] = 5.6

print(ordinary_dik) # {'height': 5.6, 'Name': 'Raghav', 'Age': 21}

print(ordinary_dik.values()) # dict_values(['Raghav', 21, 5.6])

print(ordinary_dik.keys()) # dict_keys(['Name', 'Age', 'height'])

for k, v in ordinary_dik.items():
    print(k, ":", v)


# ordinary_dik_new with same elements but in diffrent order
ordinary_dik_new = {'height': 5.6, 'Name': 'Raghav', 'Age': 21}

'''
    If two dictionaries are same but in different order, comparing them 
    will return True while comparing two OrderDicts with same items 
    but in diffrent order will return False﻿
'''
print(ordinary_dik == ordinary_dik_new) # True
print(OrderedDict(ordinary_dik) == OrderedDict(ordinary_dik_new))   # False
