from functools import partial


def add(x, y, z):
    return x + y + z


f = partial(add, 1, 2)
print(f(3))
