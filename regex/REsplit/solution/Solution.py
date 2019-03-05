'''
https://www.hackerrank.com/challenges/re-split/problem
DONE
'''

regex_pattern = r"[,\\.]"  # Do not delete 'r'.

from re import split


# re.split(pattern, string, maxsplit=0, flags=0)
def run():
    # for _str in split(regex_pattern, input()):
    # print(_str)
    print("\n".join(split(regex_pattern, input())))


if __name__ == '__main__':
    run()
