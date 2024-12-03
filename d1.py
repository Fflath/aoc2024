from parser import *


with open("d1.txt", "r") as f:
    inp = f.read()


input = Parser(inp)


def mappend(acc, addition):
    for idx, _ in enumerate(acc):
        acc[idx].append(addition[idx])


def acc2(acc, addition):
    print(acc)
    print(addition)
    ls = acc[0], ds = acc[1]
    ds[addition[1]] = ds.get(addition, 0) + 1
    ls.append(addition[0])
    print(acc)
    print("-------------")


def line():
    return mapper(sequence([integer(), ws(), integer(), nl()]), lambda x: (x[0], x[2]))


def file(acc):
    accumulator(line(), lambda res, acc: mappend(acc, res), acc)(input)
    return acc


def f2(acc):
    accumulator(line(), lambda res, acc: acc2(acc, res), acc)(input)
    return acc


def p1():
    f, s = file([[], []])
    f.sort(), s.sort()
    sum = 0
    for idx, _ in enumerate(f):
        sum += abs(f[idx] - s[idx])
    return sum


def p2():
    ls, ds = f2([[], {}])
    sum = 0
    for _, x in enumerate(ls):
        sum += x * ds.get(x, 0)
    return sum
