#!/usr/bin/env python3.8


def get_data():
    with open('puzzle_input') as infile:
        data = [i.rstrip() for i in infile.readlines()]

    return data


def get_test():
    with open('test_input') as infile:
        data = [i.rstrip() for i in infile.readlines()]

    return data


def solve(data):
    for _ in range(0, 5):
        data = update(data)

    count = 0
    for row in data:
        count += row.count('#')

    return count


def update(data):
    new_data = []
    max_row = len(data) - 1
    max_col = len(data[0]) - 1
    for rindex in range(0, len(data)):
        new_row = ''
        row = data[rindex]
        for cindex in range(0, len(row)):
            seat = data[rindex][cindex]
            if seat == '.':
                new_row += seat
                continue

            ns = get_n(rindex, cindex, max_row=max_row, max_col=max_col)
            occupied = [i for i in ns if data[i[0]][i[1]] == '#']
            if len(occupied) >= 4:
                new_row += 'L'
            elif len(occupied) == 0:
                new_row += '#'
            else:
                new_row += seat

        new_data.append(new_row)

    return new_data


def get_n(row, column, max_row, max_col):
    poss = []
    if row == 0:
        poss_rows = [row, row + 1]
    elif row == max_row:
        poss_rows = [row, row - 1]
    else:
        poss_rows = [row, row - 1, row + 1]

    for poss_row in poss_rows:
        if column == 0:
            poss.append((poss_row, column + 1))
            poss.append((poss_row, column))
        elif column == max_col:
            poss.append((poss_row, column - 1))
            poss.append((poss_row, column))
        else:
            poss.append((poss_row, column - 1))
            poss.append((poss_row, column))
            poss.append((poss_row, column + 1))

    poss.remove((row, column))
    to_remove = []
    for i in poss:
        if i[0] > max_row:
            to_remove.append(i)
        elif i[1] > max_col:
            to_remove.append(i)

    poss = [i for i in poss if i not in to_remove]
    return poss


def solve2():
    pass


if __name__ == '__main__':
    data = get_data()
    test = get_test()
    print(f'Test: {solve(test)}')
    print(f'Part1: {solve(data)}')
    print(f'Part2: {solve2()}')
