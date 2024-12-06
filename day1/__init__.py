from collections import Counter as counter


def solution1(xs, ys):
    i = 0
    total = 0

    while i < len(xs):
        total += abs(xs[i] - ys[i])
        i += 1

    return total


def solution2(xs, ys):
    counting = counter(ys)
    total = 0

    for x in xs:
        total += x * counting.get(x, 0)

    return total
