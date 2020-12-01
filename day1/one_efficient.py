#!/usr/bin/env python3

import math


TARGET = 2020


def get_data() -> list:
    with open('puzzle_input') as infile:
        data = infile.readlines()

    return [int(i.rstrip()) for i in data]


def get_answer():
    data = get_data()

    for num1 in data:
        leftover = TARGET - num1
        sliced = get_slice(num1, data)
        possible = [i for i in sliced if i <= leftover]
        for num2 in possible:
            if sum([num1, num2]) == TARGET:
                return math.prod([num1, num2])


def get_slice(num: int, data: list):
    index = data.index(num)
    if index == 0:
        return data[1:]
    elif index == len(data) - 1:
        return data[0:-1]
    else:
        return data[0:index] + data[index + 1:]


if __name__ == '__main__':
    print(get_answer())
