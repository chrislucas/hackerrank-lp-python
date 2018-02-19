#https://brilliant.org/wiki/trailing-number-of-zeros/

'''
Contando os mutiplos de 5, 25, 123, ... ate que 5 ^ k < n
'''
from math import floor, log10


def countTrailingZerosFactorialV1(nFactorial):
    acc = 0
    divisor = 5
    while divisor < nFactorial:
        acc += nFactorial // divisor
        divisor *= 5
    return acc


def log(logt, base):
    return log10(logt) / log10(base)


def countTrailingZerosFactorialV2(nFactorial):
    k = int(floor(log(nFactorial, 5)))
    acc = 0
    divisor = 5
    for i in range(0, k):
        acc += int(floor(nFactorial / divisor))
        divisor *= 5
    return acc


def printResultsAssesment(value):
    print("%d: %d %d" % (value
                     ,countTrailingZerosFactorialV1(value)
                    ,countTrailingZerosFactorialV2(value)))


printResultsAssesment(1000)
printResultsAssesment(500)
printResultsAssesment(777)
printResultsAssesment(60)


print(countTrailingZerosFactorialV1(19) + countTrailingZerosFactorialV1(59) + countTrailingZerosFactorialV1(158))


if __name__ == '__main__':
    pass