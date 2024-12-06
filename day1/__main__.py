from . import solution1, solution2
from sys import argv


if len(argv) - 1:
    with open(argv[1], 'r') as file:
        list1 = []
        list2 = []

        for line in file:
            a, b = map(int, line.strip().split('   '))
            list1.append(a)
            list2.append(b)

        print(solution1(sorted(list1), sorted(list2)))
        print(solution2(sorted(list1), sorted(list2)))

else:
    e1 = sorted([3, 4, 2, 1, 3, 3])
    e2 = sorted([4, 3, 5, 3, 9, 3])

    print('Testing solution1')
    result = solution1(e1, e2)
    expected = 11
    assert result == expected, f'expected `{expected}`, got `{result}`'
    print('OK!')

    print('Testing solution2')
    result = solution2(e1, e2)
    expected = 31
    assert result == expected, f'expected `{expected}`, got `{result}`'
    print('OK!')
