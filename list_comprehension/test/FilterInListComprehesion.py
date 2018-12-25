'''
https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s11.html
https://docs.quantifiedcode.com/python-anti-patterns/readability/using_map_or_filter_where_list_comprehension_is_possible.html
'''


def test_filter_1():
    _list = [i for i in range(0, 1000) if (i & 1) == 0]
    print(_list)


# https://www.hackerrank.com/challenges/list-comprehensions/problem
def test_filter_2(x, y, z, n):
    _mat = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1) if (i + j + k) != n]
    print(_mat)


def test_map_filter_fn():
    _list = [_ for _ in range(0, 1000)]
    _transformed = list(map(lambda x: x * x, filter(lambda x: x & 1 == 1, _list)))
    print(_transformed)


# test_filter_2(1, 1, 1, 2)
# test_filter_2(2, 2, 2, 2)


test_map_filter_fn()

if __name__ == '__main__':
    pass
