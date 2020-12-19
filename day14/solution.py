#!/usr/bin/env python3.8

import collections
import itertools
import multiprocessing
import re


PERMS = {}


def get_test_data():
    with open('test_input') as infile:
        return [i.rstrip() for i in infile.readlines()]


def get_test2_data():
    with open('test2_input') as infile:
        return [i.rstrip() for i in infile.readlines()]


def get_data():
    with open('puzzle_input') as infile:
        return [i.rstrip() for i in infile.readlines()]


def decimal_to_bin(n):
    binary = bin(int(n)).replace('0b', '')
    return str(binary).zfill(36)


class Numby(object):
    def __init__(self, dec=0):
        self.as_list = None
        self.dec_to_array(dec)

    def dec_to_array(self, dec):
        binary = bin(int(dec)).replace('0b', '')
        full = binary.zfill(36)
        self.as_list = [i for i in full]

    @property
    def as_dec(self):
        return int(''.join(self.as_list), 2)

    @property
    def as_str(self):
        return ''.join(self.as_list)

    def set_by_dec(self, dec):
        self.dec_to_array(dec)

    def set_by_str(self, stringed):
        self.as_list = [i for i in stringed]


class Shifter(object):
    def __init__(self):
        self.array = collections.defaultdict(Numby)
        self.mask = []

    def set_mask(self, mask):
        self.mask = [i for i in mask]

    def set_mem_slot(self, slot, value):
        new_num = Numby(value)
        as_list = new_num.as_list

        for index in range(36):
            mask_val = self.mask[index]
            if mask_val != 'X':
                as_list[index] = mask_val

        self.array[slot] = new_num

    def get_mem_slot_as_int(self, slot):
        return self.array[slot].as_dec

    def get_total(self):
        return sum([i.as_dec for i in self.array.values()])


def check_option(packaged):
    option, as_list, mask = packaged
    option = list(option)
    new_list = as_list.copy()

    for index in range(len(new_list)):
        if mask[index] == 'X':
            # print(f'found X at index {index} in mask')
            popper = option.pop()
            new_list[index] = popper
        elif mask[index] == '1':
            new_list[index] = '1'
        else:
            new_list[index]

    new_list_str = ''.join(new_list)
    # print(f'got a new option: {new_list}')
    this_num = Numby()
    this_num.set_by_str(new_list_str)

    return this_num.as_dec


class Shifter2(Shifter):
    def __init__(self):
        super().__init__()
        self.array = {}
        self.errors = []

    def set_mem_slot(self, slot, value):
        new_num = Numby(slot)
        as_list = new_num.as_list

        x_count = self.mask.count('X')
        # print(f'found {x_count} xs in {self.mask}')
        if x_count in PERMS:
            poss = PERMS[x_count]
        else:
            poss = [
                ''.join(i) for i in itertools.product('01', repeat=x_count)
            ]

        # print(f'found {len(poss)} possibilities, expecting {2 ** x_count}')
        # print(poss)
        map_args = [[i, as_list, self.mask] for i in poss]
        with multiprocessing.Pool(10) as p:
            result = p.map(check_option, map_args)

        for item in result:
            self.array[item] = int(value)

    def get_total(self):
        total = sum(self.array.values())
        return total


def solve(data, shift):
    count = 1
    for line in data:
        print(f'starting to solve line {count}')
        if line.startswith('mask'):
            print(line)
            shift.set_mask(line.split()[-1])
        else:
            slot, value = parse_line(line)
            # print(f'line {line} parsed as {slot} {value}')
            shift.set_mem_slot(slot, value)

        count += 1

    return shift.get_total()


def solve_test():
    data = get_test_data()
    shift = Shifter()
    return solve(data, shift)


def parse_line(line):
    res = re.search(r'mem\[([0-9]+)\] = ([0-9]+)', line)
    return res.groups()


def solve_1():
    data = get_data()
    shift = Shifter()
    return solve(data, shift)


def solve_2():
    data = get_data()
    shift = Shifter2()
    return solve(data, shift)


def solve_test2():
    data = get_test2_data()
    shift = Shifter2()
    return solve(data, shift)


if __name__ == '__main__':
    # populate_perms()
    # print(f'Test: {solve_test()}')
    # print(f'Part1: {solve_1()}')
    print(f'Part2: {solve_2()}')
    # print(f'Test2: {solve_test2()}')
