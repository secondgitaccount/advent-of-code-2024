from . import middle, ordering_rules, pages_ordering, solution1, solution2, sort, valid_ordering
from sys import argv


if len(argv) - 1:
    with open(argv[1], 'r') as file:
        print(solution1(file))

    with open(argv[1], 'r') as file:
        print(solution2(file))

else:

    source = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

    it = (line for line in source.split('\n'))
    before_rules, after_rules = ordering_rules(it)
    pages = pages_ordering(it)

    print('Testing First Problem')

    print(' Testing ordering_rules')

    result = ordering_rules((n for n in []))
    expected = {}, {}
    assert result == expected, f'expected `ordering_rules` of empty to be `{expected}`, got `{result}`'

    rules = ['1|2']
    result = ordering_rules((n for n in rules))
    expected = {1: [2]}, {2: [1]}
    newline = '\n'
    assert result == expected, f'''expected `ordering_rules` of `{newline.join(rules)}`to be `{expected}`, got `{result}`'''

    rules = ['1|2', '1|3', '10|1']
    result = ordering_rules((n for n in rules))
    expected = {1: [2, 3], 10: [1]}, {1: [10], 2: [1], 3: [1]}
    newline = '\n'
    assert result == expected, f'''expected `ordering_rules` of `{newline.join(rules)}`to be `{expected}`, got `{result}`'''

    print(' OK!') 

    print(' Testing middle_page')
    middle_pages = [61, 53, 29, 47, 13, 75]

    for i, page in enumerate(pages):
        result = middle(page)
        expected = middle_pages[i]
        assert result == expected, f'expected `middle_page` of `{page}` to be `{expected}`, got `{result}`'

    print(' OK!')

    print(' Testing valid_ordering')
    right_ordering = pages[:3]
    wrong_ordering = pages[3:]

    for ordering in right_ordering:
        expected = True, ''
        result = valid_ordering(ordering, before_rules, after_rules)
        assert result == expected, f'expected `valid_ordering` of `{ordering}` to be `{expected}`, got `{result}`'

    for ordering in wrong_ordering:
        expected = False
        result = valid_ordering(ordering, before_rules, after_rules)
        assert result[0] == expected, f'expected `valid_ordering` of `{ordering}` to be a tuple `({expected}, _)` where `_` is the reason, got `{result}`'

    print(' OK!')

    print(' Testing solution1')
    it = (line for line in source.split('\n'))
    result = solution1(it)
    expected = 143
    assert result == expected, f'expected `{expected}`, got `{result}`'

    print(' OK!')
    print('OK!')


    print('Testing Second Problem')

    print(' Testing sort')
    it = (line for line in source.split('\n'))
    before_rules, after_rules = ordering_rules(it)

    ordering = [75,97,47,61,53]
    expected = [97,75,47,61,53]
    result = sort(ordering, before_rules, after_rules)
    assert result == expected, f'expected `{expected}` to be the sorted of `{ordering}`, got `{result}`'

    ordering = [61,13,29]
    expected = [61,29,13]
    result = sort(ordering, before_rules, after_rules)
    assert result == expected, f'expected `{expected}` to be the sorted of `{ordering}`, got `{result}`'

    ordering = [97,13,75,29,47]
    expected = [97,75,47,29,13]
    result = sort(ordering, before_rules, after_rules)
    assert result == expected, f'expected `{expected}` to be the sorted of `{ordering}`, got `{result}`'

    print(' OK!')

    print(' Testing solution2')
    it = (line for line in source.split('\n'))

    expected = 123
    result = solution2(it)
    assert result == expected, f'expected `{expected}`, got `{result}`'
    print(' OK!')

    print('OK!')
