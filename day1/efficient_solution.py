#!/usr/bin/env python3

import sys


def get_answer(target: int, total_nums: int = 2, data: list = None) -> int:
    if data is None:
        with open('puzzle_input') as infile:
            data = [int(i.rstrip()) for i in infile.readlines()]

    filtered = [i for i in data if i < target + total_nums]
    for num in filtered:
        leftover = target - num

        if total_nums > 2:
            sliced = get_slice(filtered.index(num), filtered)
            result = get_answer(leftover, total_nums - 1, sliced)
            if result:
                return num * result

        if leftover in data and (leftover != num or data.count(num) > 1):
            return num * leftover


def get_slice(index: int, data: list):
    if index == 0:
        return data[1:]
    elif index == len(data) - 1:
        return data[0:]
    else:
        return data[0:index] + data[index + 1:]


if __name__ == '__main__':
    with open('puzzle_input') as infile:
        data = [int(i.rstrip()) for i in infile.readlines()]
    print(get_answer(2020, int(sys.argv[1]), data))
