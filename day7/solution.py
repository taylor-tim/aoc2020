#!/usr/bin/env python3.8

import itertools


def get_data():
    with open('puzzle_input') as infile:
        data = infile.readlines()
    return data


def can_contain(data, search):
    acc = []
    for line in data:
        source = source_bag(line)
        if search in line and source != search:
            print(f'found {search} in {line}, source is {source}')
            acc.append(source)

    return acc


def source_bag(line):
    return line.split(' bags')[0]


def solve2():
    data = get_data()
    search = [(1, 'shiny gold')]
    bags = {}
    for line in data:
        res = parse_line(line)
        bags.update(res)

    total = []

    while True:
        prev = total.copy()
        search = get_contains(search, bags)
        total.extend(search)
        if total == prev:
            break

    return total, sum([i[0]for i in total])


def get_contains(bag_list, bags):
    total = []
    for bag_data in bag_list:
        bag = bag_data[-1]
        bag_num = bag_data[0]
        if bag in bags:
            total.extend(bags[bag] * int(bag_num))

    return total

def parse_line(line):
    splits = line.split()
    source = ' '.join(splits[0:2])
    result = []
    for index in range(0, len(splits)):
        word = splits[index]
        try:
            num = int(word)
        except:
            continue
        bag = ' '.join(splits[index + 1: index +3])
        result.append((num, bag))

    return {source: result}


def solve():
    data = get_data()
    search = 'shiny gold'

    total = set()
    new_group = ['shiny gold']

    while True:
        ugh = [can_contain(data, i) for i in new_group]
        new_group = list(itertools.chain(*ugh))
        if not new_group:
            break
        else:
            total = total.union(new_group)

    return total


if __name__ == '__main__':
    print(len(solve()))
