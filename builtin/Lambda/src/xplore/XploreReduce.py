from functools import reduce


def summation():
    return reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])


print(summation())

if __name__ == "__main__":
    pass
