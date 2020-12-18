#!/usr/bin/env python3.8


def get_test_data():
    with open('test_input') as infile:
        return [i.rstrip() for i in infile.readlines()]


def get_data():
    with open('puzzle_input') as infile:
        return [i.rstrip() for i in infile.readlines()]


def solve_test():
    data = get_test_data()
    shipper = Shippy()
    return shipper.process_data(data)


def solve_1():
    data = get_data()
    shipper = Shippy()
    return shipper.process_data(data)


def solve_2():
    data = get_data()
    wp = WayPointer()
    return wp.process_data(data)


class WayPointer(object):
    def __init__(self):
        self.x = 10
        self.y = 1
        self.ship_x = 0
        self.ship_y = 0
        self.direction = 0

    def process_data(self, data):
        for line in data:
            letter = line[0]
            number = int(line[1:])

            if letter == 'N':
                self.y += number

            elif letter == 'E':
                self.x += number

            elif letter == 'S':
                self.y -= number

            elif letter == 'W':
                self.x -= number

            elif letter in ['L', 'R']:
                self.rotate(letter, number)

            elif letter == 'F':
                move_x = self.ship_x + (self.x * number)
                move_y = self.ship_y + (self.y * number)
                self.ship_x = move_x
                self.ship_y = move_y

        total = sum([abs(i) for i in [self.ship_x, self.ship_y]])
        return total

    def rotate(self, direction: str, degrees: int):
        turn_times = int(degrees / 90)
        if direction == 'L':
            turn_times = 4 - turn_times

        for _ in range(0, turn_times):
            self.rotate_right()

    def rotate_right(self):
        newx, newy = self.y, self.x
        self.direction += 1
        self.direction = self.direction % 4

        if self.direction == 0:
            newy = abs(newy)
        elif self.direction == 1:
            newy = 0 - newy
        elif self.direction == 2:
            newy = 0 - newy
        else:
            newy = abs(newy)

        self.x = newx
        self.y = newy


class Shippy(object):
    directions = {
        0: 'north',
        1: 'east',
        2: 'south',
        3: 'west'
    }

    def __init__(self):
        self.facing = 1
        self.x = 0
        self.y = 0

    def rotate(self, direction: str, degrees: int):
        turn_times = int(degrees / 90)
        if direction == 'L':
            self.facing -= turn_times % 4
        else:
            self.facing += turn_times % 4

        while self.facing >= 4:
            self.facing -= 4

        while self.facing <= -1:
            self.facing += 4

    def move_forward(self, distance: int):
        if self.facing == 0:
            self.y += distance
        elif self.facing == 2:
            self.y -= distance
        elif self.facing == 1:
            self.x += distance
        elif self.facing == 3:
            self.x -= distance

    def where_am_i(self):
        print(f'now at {self.x}:{self.y}')

    def move_north(self, distance: int):
        self.y += distance

    def move_south(self, distance: int):
        self.y -= distance

    def move_east(self, distance: int):
        self.x += distance

    def move_west(self, distance: int):
        self.x -= distance

    def process_data(self, data):
        for line in data:
            letter = line[0]
            number = int(line[1:])

            if letter in ['L', 'R']:
                self.rotate(letter, number)

            if letter == 'N':
                self.move_north(number)

            if letter == 'S':
                self.move_south(number)

            if letter == 'E':
                self.move_east(number)

            if letter == 'W':
                self.move_west(number)

            if letter == 'F':
                self.move_forward(number)

        return sum([abs(i) for i in [self.x, self.y]])


if __name__ == '__main__':
    assert 25 == solve_test()
    print(f'Test: {solve_test()}')
    assert solve_1() == 381
    print(f'Part1: {solve_1()}')
    print(f'Part2: {solve_2()}')
