'''
https://www.hackerrank.com/challenges/no-idea/problem
'''


def sv1(set_a, set_b, numbers):
    acc = 0
    for val in numbers:
        if val in set_a:
            acc += 1
        if val in set_b:
            acc -= 1
    return acc


def sv2(set_a, set_b, numbers):
    anb = (set_a - (set_a & set_b))
    bna = (set_b - (set_a & set_b))
    acc = 0
    for i in numbers:
        if i in anb:
            acc += 1
        if i in bna:
            acc -= 1
    return acc


def run():
    n, m = tuple(map(int, input().split(" ")))
    numbers = input().split(" ")
    set_a = set(input().split(" "))
    set_b = set(input().split(" "))
    print(sv2(set_a, set_b, numbers))


def test():
    sv2({1, 3, 7}, {1, 3, 4, 5}, [])
    sv2({1, 3}, {5, 7}, [])


if __name__ == '__main__':
    run()
