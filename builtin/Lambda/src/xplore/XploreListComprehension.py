# https://www.python-course.eu/python3_list_comprehension.php


# generator expression

genObject = (x for x in range(10))
'''
print(genObject)
print(type((genObject)))
print(list(genObject))
'''


def primes(n):
    from math import sqrt
    np = [j for i in range(2, int(sqrt(n))+1) for j in range(i*i, n, i)]
    pp = [i for i in range(0, n) if i not in np and i > 1]
    return pp


_k = primes(1000)
print(_k, len(_k))


if __name__ == '__main__':
    pass