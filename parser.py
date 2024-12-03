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


def run():
    input = Parser("123    456\n456    123\n")
    print(parse(input))


def parse(input):
    parser = digit()
    return parser(input)


def char():
    def p(input):
        return input.next()

    return p


def satisfy(parser, acceptor):
    def p(input):
        head = input.head
        res = parser(input)
        if acceptor(res):
            return res
        else:
            input.head = head
            raise Exception("rejected by satisfy")

    return p


def digit():
    return satisfy(char(), lambda x: x in "0123456789")


def ascii_letter():
    return satisfy(
        char(), lambda x: x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )


def choice(parsers):
    def p(input):
        head = input.head
        for parser in parsers:
            try:
                return parser(input)
            except:
                input.head = head
        raise Exception("rejected by choice")

    return p


def many(parser):
    def p(input):
        res = []
        while True:
            head = input.head
            try:
                res.append(parser(input))
            except:
                input.head = head
                break
        return res

    return p


def sequence(parsers):
    def p(input):
        res = []
        for parser in parsers:
            try:
                res.append(parser(input))
            except:
                raise Exception("sequence failed")
        return res

    return p


def mapper(parser, func):
    def p(input):
        return func(parser(input))

    return p


def accumulator(parser, func, acc):
    def p(input):
        while True:
            h = input.head
            try:
                func(parser(input), acc)
            except:
                input.head = h
                break
        return acc

    return p


def digits():
    return mapper(sequence([digit(), many(digit())]), lambda x: "".join([x[0]] + x[1]))


def integer():
    return mapper(digits(), lambda x: int(x))


def ws():
    return many(satisfy(char(), lambda x: x in " \t"))


def nl():
    return satisfy(char(), lambda x: x == "\n")
