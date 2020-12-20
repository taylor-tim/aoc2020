#!/usr/bin/env python3.8

import math
import re


def get_test_data():
    with open('test_input') as infile:
        return [i.rstrip() for i in infile.readlines()]


def get_data():
    with open('puzzle_input') as infile:
        return [i.rstrip() for i in infile.readlines()]


def simple_parse(data):
    rules = {}
    tickets = []
    for line in [i for i in data if i]:
        comp = re.compile(r'([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)')
        res = comp.search(line)
        if res:
            name, start1, end1, start2, end2 = res.groups()
            rules[name] = {
                'start1': int(start1),
                'end1': int(end1),
                'start2': int(start2),
                'end2': int(end2)
            }

        else:
            try:
                nums = [int(i) for i in line.split(',')]
            except ValueError:
                continue

            tickets.append(nums)

    return rules, tickets


def solve_2():
    data = get_data()
    rules, tickets = simple_parse(data)
    valid = []
    for ticket in tickets[1:]:
        if filter_tickets(ticket, rules):
            valid.append(ticket)

    valid2 = [i for i in tickets if valid_ticket(i)]
    print(len(valid))
    print(len(valid2))

    invalid2 = []
    invalidnum2s = []
    for i in range(0, len(tickets)):
        if tickets[i] not in valid2:
            invalidnum2s.append(i)
            invalid2.append(tickets[i])

    invalid_nums = []
    for ticket in invalid2:
        for num in ticket:
            if num <= 30 or num >= 971:
                invalid_nums.append(num)

    print(f'{sum(invalid_nums)}')
    print(f'invalid: {len(invalid2)}')
    print(f'valid: {len(valid2)}')
    print(f'diff {len(tickets) - len(invalid2)}')

    order = {}
    print(rules)

    possible_rows = list(range(0, len(tickets[0])))

    while len(possible_rows) > 0:
        for name, valid_range in rules.items():
            poss = []
            for index in possible_rows:
                row = [x[index] for x in valid]
                # print(row)
                res = [check_item(valid_range, i) for i in row]

                if all(res):
                    poss.append(index)

            if len(poss) == 1:
                order[name] = poss[0]
                possible_rows.remove(poss[0])

    my_ticket = tickets[0]
    mult = []
    print(order)
    for name, row in order.items():
        if 'departure' in name:
            mult.append(my_ticket[row])

    answer = math.prod(mult)
    return answer


def valid_ticket(ticket):
    return all([31 <= i <= 970 for i in ticket])


def filter_tickets(ticket, rules):
    valid_nums = []
    for num in ticket:
        for rule in rules.values():
            res = check_item(rule, num)
            if res:
                valid_nums.append(num)
                break

    valid = len(valid_nums) == len(ticket)
    if not valid:
        invalid_nums = set(ticket).difference(valid_nums)
        print(f'invalid ticket: {ticket} ({invalid_nums})')

    return valid


def check_item(ranges, item):
    if ranges['start1'] <= item <= ranges['end1']:
        return True
    elif ranges['start2'] <= item <= ranges['end2']:
        return True

    return False


if __name__ == '__main__':
    print(f'Part2: {solve_2()}')
