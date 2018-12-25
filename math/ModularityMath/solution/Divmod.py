'''
https://www.hackerrank.com/challenges/python-mod-divmod/problem?h_r=next-challenge&h_v=zen
'''
def run():
    p = int(input())
    q = int(input())
    s = divmod(p, q)
    print("%d\n%d\n%s" % (s[0], s[1], s))


if __name__ == '__main__':
    run()
