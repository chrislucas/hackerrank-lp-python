from functools import reduce


def testfnzip():
    a = [1, 2, 3, 4, 5, 6]
    b = ["a", "b", "c", "d", "e", "f"]
    c = [0x10, 0xff, 0x32, 0x7f, 0x86]
    zipped = zip(a, b, c)
    print(*zipped)
    print(type(zipped))
    x = [a] + [b] + [c]
    # x = a + b + c
    print(*zip(x))


matrix = []
n, lines = [int(x) for x in input().rstrip().split(' ')]
for i in range(0, lines):
    matrix += [[float(x) for x in input().rstrip().split(' ')]]
    #matrix.append([float(x) for x in input().rstrip().split(' ')])


it = zip(*matrix)
for i in it:
    print(reduce(lambda x, y: x + y, i) / len(i))

if __name__ == "__main__":
    pass
