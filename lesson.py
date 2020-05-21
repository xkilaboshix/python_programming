import functools


def d(f):
    @functools.wraps(f)
    def wrapper():
        """Wrapper docstring"""
        print('くぁwせdrftgyふじこlp')
        return f()
    return wrapper

@d
def shimarin():
    """shimarin docstring"""
    print('死んじまったじゃねえか')

# shimarin()
print(shimarin.__doc__)
# help(shimarin)
