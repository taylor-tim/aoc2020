#!/usr/bin/env python3

import itertools
import math


def get_data() -> list:
    with open('puzzle_input') as infile:
        data = infile.readlines()

    return [int(i.rstrip()) for i in data]


def get_answer() -> int:
    data = get_data()
    perms = itertools.permutations(data, 2)
    for pair in perms:
        if sum(pair) == 2020:
            return math.prod(pair)


if __name__ == '__main__':
    print(get_answer())
