#!/usr/bin/env python3.8


def get_data() -> list:
    with open('puzzle_input') as infile:
        return [i.rstrip() for i in infile.readlines()]


def parse_data(data: list) -> dict:
    result = []

    for line in data:
        times, letter, passwd = line.split()
        min_times, max_times = times.split('-')
        result.append({
            'min': int(min_times),
            'max': int(max_times),
            'letter': letter[0],
            'passwd': passwd
        })
    return result


def count_valid() -> int:
    data = get_data()
    parsed = parse_data(data)

    valid = 0

    for item in parsed:
        count = item['passwd'].count(item['letter'])
        needed = [i for i in range(item['min'], item['max'] + 1)]
        if count in needed:
            valid += 1

    return valid


if __name__ == '__main__':
    print(count_valid())
