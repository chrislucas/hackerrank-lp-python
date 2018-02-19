from math import sin, cos, tan, pi, acos, atan

# lambda => lambda argument_list: expression
# map (func, seq [] )
p = map(lambda x: (x ^ (x - 1)), [2, 3, 4, 5, 6, 7])

print(list(p))


def mapFunctions(value, functions):
    res = []
    for fn in functions:
        res.append(fn(value * pi / 180.0))
    return res


def mapFunctionsListComprehension(value, functions):
    return [fn(value * pi / 180.0) for fn in functions]


def mapTrigonometryFunctions(value):
    return map(lambda fn: fn(value * pi / 180), [sin, cos, tan, acos, atan])


def testMapFnTrig():
    print([i for i in mapTrigonometryFunctions(45)])


#print(type(()))
print(mapFunctions(45, (sin, cos, tan)))
#print(type([]))
print(mapFunctionsListComprehension(45, [sin, cos, tan]))
testMapFnTrig()


if __name__ == "__main__":
    pass
