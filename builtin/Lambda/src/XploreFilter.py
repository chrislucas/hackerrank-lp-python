T = [1, 2, 3, 4, 5]


def filter_list_even(T):
    return filter(lambda x: even(x), T)


def even(x):
    return (x & 1) == 0


f = filter_list_even(T)

print(type(f))
print(*f)


if __name__ == "__main__":
    pass
