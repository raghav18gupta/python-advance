dic = dict(zip(['a', 'b', 'c', 'd'], [1, 2, 3, 4]))
print(dic)
try:
    b = dic['e']
except Exception as e:
    b = e
    print(e)

try:
    b = dic['s']
except KeyError as e:
    dic['s'] = 12

try:
    x = dic['h']
except:
    dic['h'] = 17

print(b)
print('lala')
