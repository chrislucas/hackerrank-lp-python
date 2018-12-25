'''
https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
'''


def test():
    data = [
        [{1, 2, 3}, {2, 3, 4}]
        , [{1, 2, 3, 5}, {2, 3, 4, 7}]
        , [set("Hacker"), set("Rank")]
        , [set("Hacker"), {'R', 'a', 'n', 'k'}]
    ]
    idx = 3
    print(data[idx][0] ^ data[idx][1])


def run():
    n = input()
    english_subscribe = set(input().split(" "))
    n = input()
    french_subscribe = set(input().split(" "))
    print(len(english_subscribe ^ french_subscribe))


if __name__ == '__main__':
    run()
