#!/usr/bin/env python3.8

import re


def get_data() -> str:
    with open('puzzle_input') as infile:
        data = infile.read()
    return data


def parse_data(data: str) -> list:
    passports = []

    splits = data.split('\n\n')
    for line in [i.rstrip() for i in splits]:
        consistent = line.replace('\n', ' ')
        groups = consistent.split()
        passport = PassPort()

        for item in groups:
            k, v = item.split(':', 2)
            if k in ['byr', 'iyr', 'eyr']:
                try:
                    v = int(v)
                except ValueError:
                    v = 0
            elif k == 'hgt':
                v = convert_hgt(v)
            passport[k] = v

        passports.append(passport)

    return passports


def convert_hgt(value: str):
    if value.endswith('cm'):
        return int(value.replace('cm', ''))

    elif value.endswith('in'):
        return int(round(int(value.replace('in', '')) * 2.54))

    return 0


class PassPort(dict):
    req = {
        'byr': {'min': 1920, 'max': 2002},
        'iyr': {'min': 2010, 'max': 2020},
        'eyr': {'min': 2020, 'max': 2030},
        'hgt': {'min': 150, 'max': 193},
        'hcl': re.compile(r'#[0-9a-f]{6}'),
        'ecl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': 9
    }

    @property
    def valid(self):
        return all([self.get(i) for i in self.req.keys()])

    @property
    def strictly_valid(self):
        int_based = ['byr', 'iyr', 'eyr', 'hgt']
        items = [
            self.req[i]['min'] <= i <= self.req[i]['max'] for i in int_based
        ]
        items.append(self.req['hcl'].match(self.get('hcl', '0')))
        items.append(str(self.get('ecl', '')) in self.req['ecl'])
        items.append(len(str(self.get('pid', '0'))) == self.req['pid'])

        return all(items)

    def validate_hgt(self):
        hgt = str(self.get('hgt', '0cm'))

        if hgt.endswith('cm'):
            return 150 <= int(hgt.replace('cm', '')) <= 193

        elif hgt.endswith('in'):
            return 59 <= int(hgt.replace('in', '')) <= 76

        return False


def solve():
    data = get_data()
    parsed = parse_data(data)
    print(f'Part 1: {len([i for i in parsed if i.valid])}')
    print(f'Part 2: {len([i for i in parsed if i.strictly_valid])}')


if __name__ == '__main__':
    solve()
