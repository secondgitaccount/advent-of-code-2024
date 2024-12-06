from . import solution1, solution2
from sys import argv


if len(argv) - 1:
    with open(argv[1], 'r') as file:
        source = file.read()
        print(solution1(source))
        print(solution2(source))

else:

    print('Testing solution1')

    example = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    expected = 161
    result = solution1(example)
    assert result == expected, f'\nexpected eval of `{example}` to be `{expected}`,\n got `{result}`'

    example = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
    expected = 2 * 4 + 5 * 5 + 11 * 8 + 8 * 5
    result = solution1(example)
    assert result == expected, f'\nexpected eval of `{example}` to be `{expected}`,\n got `{result}`'
    print('OK!')

    print('Testing solution2')

    example = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
    expected = 48
    result = solution2(example)
    assert result == expected, f'expected `{expected}`, got `{result}`'

    print('OK!')
