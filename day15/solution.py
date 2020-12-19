#!/usr/bin/env python3.8


def get_test_data():
    return [0, 3, 6]


def get_data():
    return [18, 11, 9, 0, 5, 1]


def solve(data, top_end):
    result = {}
    for i in range(1, len(data) + 1):
        result[data[i - 1]] = {'turn': i}

    prev = data[-1]
    new_num = 0
    # print(f'prev is {prev}')
    # print(result)

    for i in range(len(result) + 1, top_end + 1):
        if 'pen_turn' in result[prev]:
            new_num = result[prev]['turn'] - result[prev]['pen_turn']

            if new_num in result:
                last = result[new_num]['turn']
                result[new_num]['pen_turn'] = last
                result[new_num]['turn'] = i
            elif new_num not in result:
                result[new_num] = {'turn': i}

            prev = new_num
        else:
            prev_turn = result[0]['turn']
            result[0] = {'pen_turn': prev_turn, 'turn': i}
            prev = 0

        # print(f'turn {i} says {prev}')
        print(f'{top_end - i}')
        # print(f'at end of turn, 0 is {result[0]}')

    return new_num


def solve_test():
    data = get_test_data()
    return solve(data, 2020)


def solve_1():
    data = get_data()
    return solve(data, 2020)


def solve_2():
    data = get_data()
    return solve(data, 30000000)


if __name__ == '__main__':
    print(f'Test: {solve_test()}')
    print(f'Part1: {solve_1()}')
    print(f'Part2: {solve_2()}')
