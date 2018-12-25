'''
https://www.hackerrank.com/challenges/python-power-mod-power/problem
'''


def exp(b, e):
    if e == 0:
        return 1
    elif e == 1:
        return b
    elif e < 0:
        b, e = 1/b, -e
    acc = 1
    while e > 0:
        if e & 1 == 1:
            acc *= b
        b *= b
        e >>= 1
    return acc


def run():
    p = int(input())
    q = int(input())
    m = int(input())
    print("%d\n%d" % (exp(p, q), pow(p, q, m)))


if __name__ == '__main__':
    run()
