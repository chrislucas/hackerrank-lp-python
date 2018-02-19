from functools import reduce


def summation():
    return reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])


def sumTerms(_list, i):
    _list[i&1] = _list[i & 1] + _list[(i-1) & 1]


def fib(n):
    _list = [0, 1]
    reduce(lambda a, i: sumTerms(_list, i), [i for i in range(1, n + 1)])
    return _list


print(fib(30))

if __name__ == "__main__":
    pass
