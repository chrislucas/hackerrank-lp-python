'''
https://www.hackerrank.com/challenges/find-angle/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen
'''

from math import sqrt, asin, acos, pi, sin, cos, atan2


def run():
    ab = int(input())
    bc = int(input())
    ac = sqrt(ab * ab + bc * bc)
    # co / hip
    rs = asin(ab / ac)
    print("%d°" % int(round(rs * 180 / pi, 0)))
    print("%d°" % int(round(atan2(ab, bc) * 180 / pi, 0)))


if __name__ == '__main__':
    run()
