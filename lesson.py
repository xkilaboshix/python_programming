import functools


def f(x, y):
    return x + y


def task(f):
    print('start')
    print(f())

# def outer(x, y):
#     def inner():
#         return x + y
#     return inner

# f = outer(10, 20)
p = functools.partial(f, 10, 20)
task(p)

# task(f)
# task(lambda x, y: x + y)