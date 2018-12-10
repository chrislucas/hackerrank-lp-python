'''
https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
'''


def test_set(_str):
    print(set([t for c in _str.split(" ") for t in c if t != ' ']))


test_set(input())


def test_set_dict(_dict):
    print(set(_dict))


test_set_dict({"a": 97, "b": 98})

# print(set(enumerate(['H', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k'])))
# print(set('HackerRank'))

if __name__ == '__main__':
    pass
