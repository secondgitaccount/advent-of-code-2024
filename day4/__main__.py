from . import solution1, solution2
from sys import argv


if len(argv) - 1:
    with open(argv[1], 'r') as file:
        print(solution1(file))

    with open(argv[1], 'r') as file:
        print(solution2(file))

else:
    source = [
        'MMMSXXMASM',
        'MSAMXMSMSA',
        'AMXSXMAAMM',
        'MSAMASMSMX',
        'XMASAMXAMM',
        'XXAMMXXAMA',
        'SMSMSASXSS',
        'SAXAMASAAA',
        'MAMMMXMMMM',
        'MXMXAXMASX',
    ]

    print('Testing solution1')

    it = iter(source)
    result = solution1(it)
    expected = 18
    assert result == expected, f'expected `{expected}`, got `{result}`'

    print('OK!')

    print('Testing solution2')

    it = iter(source)
    result = solution2(it)
    expected = 9
    assert result == expected, f'expected `{expected}`, got `{result}`'

    print('OK!')
