print(int(100), hex(100), oct(100), bin(100))
print('{0:d} {0:#x} {0:#o} {0:#b}'.format(100))


for i in range(20):
    for base in 'bdX':
        print('{:5{base}}'.format(i, base=base), end=' ')
    print()