#!/usr/bin/env python3.8


def get_data():
    with open('puzzle_input') as infile:
        return [i.rstrip() for i in infile if i]


def solve():
    data = get_data()
    acc = 0
    seen_index = []
    index = 0
    while True:
        seen_index.append(index)
        next_line, acc = run_line(data[index], index, acc)
        if next_line in seen_index:
            break
        else:
            index = next_line

    return acc


def solve2():
    data = get_data()

    for index in range(0, len(data)):
        line = data[index]
        swaps = ['nop', 'jmp']
        if line[0:3] in swaps:
            new = data.copy()
            if line.startswith('nop'):
                new[index] = line.replace('nop', 'jmp')
            else:
                new[index] = line.replace('jmp', 'nop')

            try:
                return check_change(new)
            except ValueError:
                continue


def check_change(data):
    acc = 0
    seen_index = []
    index = 0

    while True:
        seen_index.append(index)
        try:
            next_line, acc = run_line(data[index], index, acc)
        except IndexError:
            return acc
        index = next_line
        if next_line in seen_index:
            raise ValueError('failed, infinite loop')


def run_line(line, index, acc):
    if line.startswith('acc'):
        acc += int(line.split()[-1])
        next_line = index + 1

    elif line.startswith('jmp'):
        distance = int(line.split()[-1])
        next_line = sum([index, distance])

    else:
        next_line = index + 1

    return next_line, acc


if __name__ == '__main__':
    print(f'Part 1: {solve()}')
    print(f'Part 2: {solve2()}')
