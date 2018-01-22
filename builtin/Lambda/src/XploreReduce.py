from functools import reduce

T = [1, 2, 3, 4, 5]

print(reduce(lambda x, y: x+y, T))

if __name__ == "__main__":
    pass
