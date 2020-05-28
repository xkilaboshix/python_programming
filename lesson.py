# def g_hello():
#     yield 'hello 1'
#     yield 'hello 2'
#     yield 'hello 3'
#
# for g in g_hello():
#     print(g)

def g_hello():
    r = yield 'hello'
    yield r

g = g_hello()
print(next(g))
print(next(g))
