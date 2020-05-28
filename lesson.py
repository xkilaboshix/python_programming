def g_hello():
    yield 'hello 1'
    yield 'hello 2'
    yield 'hello 3'

for g in g_hello():
    print(g)
