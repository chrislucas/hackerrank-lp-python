#
'''
filter(function, sequence)
function deve retornar um valor booleano

'''

import types


def filter_list_even(t):
    return filter(lambda x: even(x), t)


def even(x):
    return (x & 1) == 0


def isInstanceOfFunctionType(obj):
    return isinstance(obj, types.FunctionType)


def isInstanceOfFilter(obj):
    return isinstance(obj, filter)


filterObject = filter_list_even([1, 2, 3, 4, 5])

print(type(filterObject))           # class filter
print(filterObject)                 # filter iterator object
print([i for i in filterObject])    # list comprehension

print("S" if isInstanceOfFunctionType(even) else "N")
print("S" if isInstanceOfFilter(filterObject) else "N")


if __name__ == "__main__":
    pass
