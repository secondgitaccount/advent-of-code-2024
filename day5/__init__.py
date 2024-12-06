def ordering_rules(it):
    before_rules = {}
    after_rules = {}

    for line in it:
        if line.strip():
            if '|' in line:
                a, b = [int(n) for n in line.strip().split('|')]
                before_rules[a] = before_rules.get(a, [])
                before_rules[a].append(b)

                after_rules[b] = after_rules.get(b, [])
                after_rules[b].append(a)
        else:
            break

    return before_rules, after_rules


def pages_ordering(it):
    pages = []
    for line in it:
        pages.append([int(n) for n in line.strip().split(',') if n])

    return pages


def valid_ordering(ordering, before_rules, after_rules):

    for i, page in enumerate(ordering):
        if i:
            before = ordering[:i]
            for p in before:
                rules = before_rules.get(page, [])
                if p in rules:
                    return False, f'{p}|{page}'


        after = ordering[(i + 1):]
        for p in after:
            rules = after_rules.get(page, [])
            if p in rules:
                return False, f'{page}|{p}'

    return True, ''

def middle(xs):
    i = len(xs) // 2
    return xs[i]


def solution1(it):
    before_rules, after_rules = ordering_rules(it)
    orderings = pages_ordering(it)

    sum = 0
    for ordering in orderings:
        valid, _ = valid_ordering(ordering, before_rules, after_rules)
        if valid:
            sum += middle(ordering)

    return sum


def sort(ordering, before_rules, after_rules):
    ordered = []

    for page in ordering:
        i = 0
        rules = before_rules.get(page, [])

        if not rules:
            ordered.append(page)
        else:
            inserted = False
            while i < len(ordered):
                if ordered[i] in rules:
                    ordered.insert(i, page)
                    inserted = True
                    break
                i += 1
            if not inserted:
                ordered.append(page)

    return ordered


def solution2(it):
    before_rules, after_rules = ordering_rules(it)
    orderings = pages_ordering(it)

    sum = 0
    for ordering in orderings:
        valid, _ = valid_ordering(ordering, before_rules, after_rules)
        if not valid:
            sum += middle(sort(ordering, before_rules, after_rules))

    return sum
