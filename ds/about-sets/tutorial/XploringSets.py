'''

'''


def test_set_1():
    _list = [_ % 127 for _ in range(0, 10000)]
    _set = set(_list)
    print("%d, %d" % (len(_list), len(_set)))


def test_set_2():
    _set = {3, 1, 2}
    print(_set)
    _set.add(4)
    print(_set)
    _set.remove(1)
    print(_set)


def test_union_set():
    a = {0, 2, 4}
    b = {1, 3, 5}
    # c = a.union(b)
    c = a | b
    print(c)

'''
    a diferenca entre o conjunto A e B eh um novo conjunto
    C sem os elementos de A que aparecem em B
'''
def test_difference_set():
    print({10, 15, 30} - {15})
    print({15} - {10, 15, 30})


def test_issubset_frozenset():
    _frozen_set = frozenset([4, 1, 2, 3])
    _frozen_set = _frozen_set.union([4, 5, 6, 7])
    print(_frozen_set)

    # _set_b = _frozen_set & {1, 2, 3}
    print({1, 2, 3}.issubset(_frozen_set))
    # issubset
    print({1, 2, 3} < _frozen_set)

    # intersect
    print({1, 2, 3} & {2})
    print(frozenset({1, 2, 3} & frozenset({2})))


def test_issuperset_frozenset():
    _frozen_set = frozenset({1, 2, 3})
    print(_frozen_set.issuperset({2, 3}))


def test_union_frozenset():
    _a_e = [chr(x) for x in range(ord('a'), ord('e') + 1)]
    print(_a_e)
    _frozen_set_1 = frozenset(_a_e)
    print(_frozen_set_1)
    _f_k = [chr(x) for x in range(ord('f'), ord('k') + 1)]
    _frozen_set_2 = frozenset(_f_k)
    _frozen_set_1 |= _frozen_set_2
    print(_frozen_set_1)


test_difference_set()

if __name__ == '__main__':
    pass
