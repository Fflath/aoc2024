from collections import namedtuple

R = namedtuple('R',['success', 'value','err'])

class Parser:
    def __init__(self, input):
        self.input = input
        self.head = 0
        self.length = len(input)

    def peek(self):
        return self.input[self.head]

    def next(self):
        ret = self.peek()
        self.head += 1
        return ret

    def r(self):
        self.head = 0


test = Parser("123abc")


def char():
    def p(input):
        try:
            n = input.next()
            return True, [n], ''
        except:
            return False,[],'end of input'

    return p


def satisfy(parser, acceptor):
    def p(input):
        head = input.head
        s,v,e = parser(input)
        if s:
            if acceptor(v): return True,v,''
            else: 
                input.head = head
                return False,[],f'satiosfy failed {acceptor}'
        else:
            return s,v,e

    return p


def digit():
    return satisfy(char(), lambda x: x[0] in "0123456789")


def ascii_letter():
    return satisfy(
        char(), lambda x: x[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )

def many(parser):
    def p(input):
        res = []
        while True:
            head = input.head
            s,v,e = parser(input)
            if s: res.append(v)
            else: 
                input.head = head
                break
        return True,res,''

    return p

def sequence(parsers):
    def p(input):
        head =input.head
        res = []
        for parser in parsers:
            s,v,r = parser(input)
            if s: res.append(v)
            else: 
                input.head=head
                return False,'',f"sequence failed at parser {parser}"
        return True,res,''
    
    return p

def mapper(parser, funcs):
    def p(input):
        s,v,e = parser(input)
        if s:
            for f in funcs:
                v = f(v)
            return True,v,''
        else: 
            return s,v,e

    return p

def drop(idxs): return lambda ls: [x for idx,x in enumerate(ls) if idx not in idxs]

def accumulator(parser, acc):
    def p(input):
        while True:
            h = input.head
            try:
                acc.add(parser(input))
            except:
                input.head = h
                break
        # return acc

    return p


def digits():
    return mapper(sequence([digit(), many(digit())]), [lambda x: "".join(x[0] + x[1])])


def integer():
    return mapper(digits(), [lambda x: int(x)])


def ws():
    return many(satisfy(char(), lambda x: x in " \t"))


def nl():
    return satisfy(char(), lambda x: x == "\n")
