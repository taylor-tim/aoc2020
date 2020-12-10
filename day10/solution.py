#!/usr/bin/env python3.8


import collections


def get_data():
    with open('puzzle_input') as infile:
        data = [int(i.rstrip()) for i in infile.readlines()]
        data.sort()

    return [0] + data


def solve():
    data = get_data()
    results = {i: 0 for i in range(1, 4)}

    for index in range(0, len(data)):
        try:
            one = data[index + 1]
            two = data[index]
            diff = one - two
        except IndexError:
            diff = 3
        results[diff] += 1

    return results[1] * results[3]


def solve2():
    data = get_data()

    paths = collections.defaultdict(int)
    paths[0] = 1

    for index in range(0, len(data)):
        this = data[index]
        sliced = data[index + 1:]
        skips = can_skips(this, sliced)

        for skip in skips:
            paths[skip] += paths[this]

    return paths[data[len(data) - 1]]


def can_skips(start, data):
    result = []
    for line in data:
        if line - start <= 3:
            result.append(line)
        else:
            break
    return result


if __name__ == '__main__':
    print(f'Part1: {solve()}')
    print(f'Part2: {solve2()}')
