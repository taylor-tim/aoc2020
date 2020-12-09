#!/usr/bin/env python3.8

import itertools


def get_data():
    with open('puzzle_input') as infile:
        data = [int(i.rstrip()) for i in infile.readlines()]

    return data


def solve():
    data = get_data()

    for index in range(0, len(data)):
        new_data = set(data[index: index + 25])
        next_num = data[index + 25]
        perms = list(itertools.permutations(new_data, 2))
        sums = [sum(i) for i in perms]
        if next_num in sums:
            continue
        else:
            return next_num


def solve2(num):
    data = get_data()
    count = 0
    for index in range(0, len(data)):
        while index + count < len(data):
            sliced = data[index:index + count]
            summed = sum(sliced)
            if summed > num:
                break

            if sum(sliced) == num:
                return min(sliced), max(sliced)

            count += 1

        count = 0



if __name__ == '__main__':
    one = solve()
    print(f'Part1: {solve()}')
    two = solve2(one)
    total = sum(two)
    print(f'Part2: {two} = {total}')
