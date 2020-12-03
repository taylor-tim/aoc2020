#!/usr/bin/env python3.8

import math


def solve(step_list: list) -> int:
    results = []
    for step in step_list:
        mapping = Mapping('puzzle_input', step)
        total = [i for i in mapping if i == '#']
        results.append(len(total))

    return math.prod(results)


class Mapping(object):
    def __init__(self, puzzle_input: str, step: tuple):
        self.mapping = []
        self.step = step
        self.parse_puzzle_input(puzzle_input)

    def parse_puzzle_input(self, puzzle_input: str) -> None:
        with open(puzzle_input) as infile:
            self.mapping = [i.rstrip() for i in infile.readlines()]

    def __iter__(self):
        return Mover(self, self.step)


class Mover(object):
    def __init__(self, treemap: list, step: tuple):
        self.treemap = treemap
        self.max_width = len(treemap.mapping[0]) - 1
        self.max_length = len(treemap.mapping) - 1
        self.x = 0
        self.y = 0
        self.step = step
        self.first_iter = True

    def __next__(self) -> str:
        if self.first_iter:
            self.first_iter = False

        else:
            next_x = self.x + self.step[0]
            next_y = self.y + self.step[1]

            if next_x > self.max_width:
                next_x -= (self.max_width + 1)

            self.x = next_x
            self.y = next_y

        try:
            row = self.treemap.mapping[self.y]
            result = row[self.x]
            return result

        except IndexError:
            raise StopIteration


if __name__ == '__main__':
    print(f'Part 1: {solve([(3, 1)])}')
    print(f'Part 2: {solve([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])}')
