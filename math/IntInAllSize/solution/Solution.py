'''
https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
'''


def exp(b, e):
    if e == 0:
        return 1
    elif e < 0:
        b = 1 / b
        e = -e
    elif e == 1:
        return b
    acc = 1
    while e > 0:
        if e & 1 == 1:
            acc *= b
        b *= b
        e >>= 1

    return acc


def run():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    return exp(a, b) + exp(c, d)


def test():
    for i in range(1, int(input())):  # More than 2 lines will result in 0 score. Do not leave a blank line also
        print((10 ** i // 9) * i)


'''
https://www.hackerrank.com/challenges/triangle-quest-2/problem
http://mathworld.wolfram.com/DemloNumber.html
'''


def test_2():
    for i in range(1, int(input()) + 1):
        # More than 2 lines will result in 0 score. Do not leave a blank line also
        print(pow((pow(10, i)-1)//9, 2))


if __name__ == '__main__':
    test_2()
