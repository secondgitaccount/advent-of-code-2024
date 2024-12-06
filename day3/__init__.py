import re


MUL = 'MUL'
DO = 'DO'
DONT = 'DONT'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

rules = [
    r'''(?P<DO>do\(\))''',
    r'''(?P<DONT>don't\(\))''',
    r'''(?P<MUL>mul\((?P<LEFT>\d{1,3}),(?P<RIGHT>\d{1,3})\))''',
    r'''(?P<WS>.)'''
]

lex = re.compile(r'|'.join(rules))

def tokenize(source):
    for m in lex.finditer(source):

        instruction = m.groupdict()[MUL] or (m.groupdict()[DO] and DO) or (m.groupdict()[DONT] and DONT)
        if instruction:
            if instruction in [DO, DONT]:
                yield (instruction, (None, None))

            else:
                left = m.groupdict()[LEFT]
                right = m.groupdict()[RIGHT]
                yield (instruction, (int(left), int(right)))


def solution1(source):
    total = 0

    for instruction, (l, r) in tokenize(source):
        if not instruction in [DO, DONT]:
            total += l * r

    return total


def solution2(source):
    total = 0

    skip = False
    for instruction, (l, r) in tokenize(source):
        if skip:
            if instruction != DO:
                continue
            else:
                skip = False
        elif instruction == DONT:
            skip = True
        elif instruction == DO:
            skip = False
        else:
            total += l * r

    return total
