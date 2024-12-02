from collections import Counter as counter


e1 = sorted([3, 4, 2, 1, 3, 3])
e2 = sorted([4, 3, 5, 3, 9, 3])


def solution1(xs, ys):
    i = 0
    sum = 0

    while i < len(xs):
        sum += abs(xs[i] - ys[i])
        i += 1

    return sum

result = solution1(e1, e2)
expected = 11
assert result == expected, f'expected {expected}, got {result}'


def solution2(xs, ys):
    counting = counter(ys)
    sum = 0

    for x in xs:
        sum += x * counting.get(x, 0)

    return sum

result = solution2(e1, e2)
expected = 31
assert result == expected, f'expected {expected}, got {result}'


def solution(file):
    with open(file, 'r') as f:
        list1 = []
        list2 = []

        for line in f:
            a, b = map(int, line.split('   '))
            list1.append(a)
            list2.append(b)

        print(solution1(sorted(list1), sorted(list2)))
        print(solution2(sorted(list1), sorted(list2)))

