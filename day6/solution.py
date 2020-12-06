#!/usr/bin/env python3.8


def get_data():
    with open('puzzle_input') as infile:
        return infile.read()


def parse_data(data):
    splits = data.split('\n\n')
    return [i.split('\n') for i in splits]


def solve(union=True):
    data = get_data()
    parsed = parse_data(data)

    total = 0

    for group in parsed:
        first = group[0]
        if len(group) == 1:
            total += len(group[0])
        else:
            first_set = set(first)
            for person in group[1:]:
                if union:
                    first_set = first_set.union(person)
                else:
                    first_set = first_set.intersection(person)
            total += len(first_set)

    return total


if __name__ == '__main__':
    print(f'First: {solve()}')
    print(f'Second: {solve(union=False)}')
