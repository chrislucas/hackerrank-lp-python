'''
https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
DIBE
'''
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    _set = set(nums)
    _sum = sum(_set)
    _len = len(_set)
    print("%.3f" % (_sum / _len))