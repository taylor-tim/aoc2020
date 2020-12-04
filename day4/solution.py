#!/usr/bin/env python3.8

import re


def get_data():
    with open('puzzle_input') as infile:
        data = infile.read()
    return data


def parse_data(data: str):
    passports = []

    splits = data.split('\n\n')
    for line in [i.rstrip() for i in splits]:
        consistent = line.replace('\n', ' ')
        groups = consistent.split()
        passport = PassPort()
        for item in groups:
            k, v = item.split(':')
            passport[k] = v

        passports.append(passport)

    return passports


class PassPort(dict):
    required = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]
    optional = [
        'cid'
    ]

    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    hcl_regex = re.compile(r'#[0-9a-f]{6}')

    @property
    def valid(self):
        return all([self.get(i) for i in self.required])

    @property
    def strictly_valid(self):
        items = [
            1920 <= self.try_int(self.get('byr', 0)) <= 2002,
            2010 <= self.try_int(self.get('iyr', 0)) <= 2020,
            2020 <= self.try_int(self.get('eyr', 0)) <= 2030,
            self.validate_hgt(),
            self.validate_hcl(),
            str(self.get('ecl', '')) in self.eye_colors,
            len(str(self.get('pid', '0'))) == 9
        ]
        return all(items)

    def validate_hcl(self):
        return self.hcl_regex.match(self.get('hcl', '0'))

    def validate_hgt(self):
        hgt = str(self.get('hgt', '0cm'))
        if hgt.endswith('cm'):
            return 150 <= int(hgt.replace('cm', '')) <= 193
        elif hgt.endswith('in'):
            return 59 <= int(hgt.replace('in', '')) <= 76

        return False

    def try_int(self, value):
        try:
            return int(value)
        except ValueError:
            return 0


def solve():
    data = get_data()
    parsed = parse_data(data)
    print(f'Part 1: {len([i for i in parsed if i.valid])}')
    print(f'Part 2: {len([i for i in parsed if i.strictly_valid])}')


if __name__ == '__main__':
    solve()
