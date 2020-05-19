import collections


d = {'apple': 4, 'banana': 3, 'pear': 1, 'orange': 2}

od = collections.OrderedDict(
    sorted(d.items(), key=lambda t: t[0]))
print(od)

