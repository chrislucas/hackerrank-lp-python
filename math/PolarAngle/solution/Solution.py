'''
https://www.hackerrank.com/challenges/polar-coordinates/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
'''

from cmath import phase
from math import sqrt


def fn_phase(r, im):
    return phase(complex(r, im))


def distance(x, y):
    return sqrt(x * x + y * y)


def run():
    p = complex(input())
    _phase = fn_phase(p.real, p.imag)
    _distance = distance(p.real, p.imag)
    print("%.3f\n%.3f" % (_distance, _phase))


if __name__ == '__main__':
    run()
