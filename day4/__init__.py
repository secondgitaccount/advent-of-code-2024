def solution1(it):
    total = 0
    searched = ['XMAS', 'SAMX']

    block = [
        next(it).strip(),
        next(it).strip(),
        next(it).strip(),
        next(it).strip(),
    ]

    def count_diagonal(block):
        total = 0
        if len(block) == 4:
            first_line = block[0]
            width = len(first_line)
            indexes = [i for (i, l) in enumerate(first_line) if l in 'XS']

            for i in indexes:
                if i + 3 < width:
                    letters = [
                        block[0][i],
                        block[1][i+1],
                        block[2][i+2],
                        block[3][i+3],
                    ]

                    word = ''.join(letters)
                    if word in searched:
                        total += 1

                if i > 2:
                    letters = [
                        block[0][i],
                        block[1][i-1],
                        block[2][i-2],
                        block[3][i-3],
                    ]

                    word = ''.join(letters)
                    if word in searched:
                        total += 1

        return total


    def count_vertical(block):
        total = 0
        if len(block) == 4:
            first_line = block[0]
            indexes = [i for (i, l) in enumerate(first_line) if l in 'XS']

            for i in indexes:
                letters = [
                    block[0][i],
                    block[1][i],
                    block[2][i],
                    block[3][i],
                ]
                word = ''.join(letters)
                if word in searched:
                    total += 1

        return total


    def count_horizontal(block):
        total = 0
        first_line = block[0]
        indexes = [i for (i, l) in enumerate(first_line) if l in 'XS']
        for i in indexes:
            word = first_line[i:i+4]
            if word in searched:
                total += 1

        return total


    while len(block):
        total += count_horizontal(block)
        total += count_vertical(block)
        total += count_diagonal(block)

        block = block[1:]
        try:
            block.append(next(it).strip())
        except StopIteration:
            continue

    return total


def solution2(it):

    def count_diagonal(block):
        searched = ['MAS', 'SAM']
        total = 0
        middle = block[1]
        width = len(middle)
        indexes = [i for (i, l) in enumerate(middle) if l in 'A']

        for i in indexes:
            if i and i + 1 < width:
                letters = [
                    block[0][i-1],
                    block[1][i],
                    block[2][i+1],
                ]
                b = ''.join(letters)

                letters = [
                    block[0][i+1],
                    block[1][i],
                    block[2][i-1],
                ]
                f = ''.join(letters)

                if b in searched and f in searched:
                    total += 1

        return total


    block = [
        next(it).strip(),
        next(it).strip(),
        next(it).strip(),
    ]

    total = 0
    while len(block) == 3:
        total += count_diagonal(block)

        block = block[1:]
        try:
            block.append(next(it).strip())
        except StopIteration:
            continue

    return total
