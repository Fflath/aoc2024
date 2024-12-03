from parser import *


with open("d1.txt", "r") as f:
    inp = f.read()

input = Parser(inp)

class p1_accumulator():
    def __init__(self):
        self.l = []
        self.r = []

    def add(self,row):
        self.l.append(row[0])
        self.r.append(row[1])

    def __iter__(self):
        for idx,lx in enumerate(self.l):
            yield lx,self.r[idx]

class p2_accumulator():
    def __init__(self):
        self.l = []
        self.r = {}

    def add(self,row):
        self.l.append(row[0])
        self.r[row[1]] = self.r.get(row[1],0) + 1

    def __iter__(self):
        for idx,lx in enumerate(self.l):
            yield lx,self.r.get(lx,0)



def line():
    return mapper(sequence([integer(), ws(), integer(), nl()]), lambda x: (x[0], x[2]))


def file(acc): 
    input.r()
    accumulator(line(), acc)(input)


def p1():
    acc = p1_accumulator()
    file(acc)
    acc.l.sort()
    acc.r.sort()
    sum = 0
    for lx,rx in iter(acc):
        sum += abs(lx-rx)
    return sum


def p2():
    acc = p2_accumulator()
    file(acc)
    sum = 0
    for l,r in iter(acc):
        sum += l * r
    return sum
