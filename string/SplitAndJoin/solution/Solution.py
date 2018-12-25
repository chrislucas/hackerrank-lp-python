'''
https://www.hackerrank.com/challenges/python-string-split-and-join/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
DONE
'''

def split_and_join(line):
    # write your code here
    return "-".join(line.split(" "))


if __name__ == '__main__':
    print(split_and_join(input()))