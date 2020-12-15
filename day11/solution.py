#!/usr/bin/env python3.8


def get_data():
    with open('puzzle_input') as infile:
        data = [i.rstrip() for i in infile.readlines()]

    return data


def get_test():
    with open('test_input') as infile:
        data = [i.rstrip() for i in infile.readlines()]

    return data


def update_map(seat_map):
    new_map = []

    for rindex in range(0, len(seat_map)):
        row = seat_map[rindex]
        new_row = []
        for cindex in range(0, len(row)):
            seat = seat_map[rindex][cindex]
            seat.update(seat_map)

            new_row.append(seat)
        new_map.append(new_row)

    return seat_map


def gen_map(data):
    seat_map = []
    for rindex in range(0, len(data)):
        row = data[rindex]
        seat_row = []
        for cindex in range(0, len(row)):
            seat_row.append(Seat(rindex, cindex, data))
        seat_map.append(seat_row)

    return seat_map


def solve():
    data = get_data()
    seat_map = SeatMap(data)

    for i in range(0, 5):
        seat_map.update()

    total = seat_map.filled
    seat_map.printme()

    return total


def solve_test():
    data = get_test()
    seat_map = SeatMap(data)
    ugh = seat_map.printme()
    ugh2 = get_test_solution(1)
    for index in range(0, len(ugh)):
        one = ugh[index]
        two = ugh2[index]
        if one != two:
            pass
            # breakpoint()

    for i in range(0, 5):
        seat_map.update()
        ugh = seat_map.printme()
        ugh2 = get_test_solution(i + 2)
        for index in range(0, len(ugh)):
            one = ugh[index]
            two = ugh2[index]
            if one != two:
                pass
                # breakpoint()

    total = seat_map.filled

    return total


def get_test_solution(num):
    if num == 1:
        return [
            'L.LL.LL.LL',
            'LLLLLLL.LL',
            'L.L.L..L..',
            'LLLL.LL.LL',
            'L.LL.LL.LL',
            'L.LLLLL.LL',
            '..L.L.....',
            'LLLLLLLLLL',
            'L.LLLLLL.L',
            'L.LLLLL.LL',
        ]
    elif num == 2:
        return [
            '#.##.##.##',
            '#######.##',
            '#.#.#..#..',
            '####.##.##',
            '#.##.##.##',
            '#.#####.##',
            '..#.#.....',
            '##########',
            '#.######.#',
            '#.#####.##',
        ]
    elif num == 3:
        return [
            '#.LL.L#.##',
            '#LLLLLL.L#',
            'L.L.L..L..',
            '#LLL.LL.L#',
            '#.LL.LL.LL',
            '#.LLLL#.##',
            '..L.L.....',
            '#LLLLLLLL#',
            '#.LLLLLL.L',
            '#.#LLLL.##',
        ]
    elif num == 4:
        return [
            '#.##.L#.##',
            '#L###LL.L#',
            'L.#.#..#..',
            '#L##.##.L#',
            '#.##.LL.LL',
            '#.###L#.##',
            '..#.#.....',
            '#L######L#',
            '#.LL###L.L',
            '#.#L###.##',
        ]
    elif num == 5:
        return [
            '#.#L.L#.##',
            '#LLL#LL.L#',
            'L.L.L..#..',
            '#LLL.##.L#',
            '#.LL.LL.LL',
            '#.LL#L#.##',
            '..L.L.....',
            '#L#LLLL#L#',
            '#.LLLLLL.L',
            '#.#L#L#.##',
        ]
    elif num == 6:
        return [
            '#.#L.L#.##',
            '#LLL#LL.L#',
            'L.#.L..#..',
            '#L##.##.L#',
            '#.#L.LL.LL',
            '#.#L#L#.##',
            '..L.L.....',
            '#L#L##L#L#',
            '#.LLLLLL.L',
            '#.#L#L#.##',
        ]


def solve2():
    pass


class SeatMap(object):
    max_row = 91
    max_column = 98

    def __init__(self, text_map):
        self.seats = []
        self.start_floors = []
        for rindex in range(0, len(text_map)):
            row = text_map[rindex]
            for cindex in range(0, len(row)):
                i = row[cindex]
                if i == '.':
                    self.start_floors.append((rindex, cindex))
        for rindex in range(0, len(text_map)):
            row = text_map[rindex]
            new_row = []
            for cindex in range(0, len(row)):
                seat = Seat(rindex, cindex)
                if text_map[rindex][cindex] == '.':
                    seat.floor = True
                new_row.append(seat)

            self.seats.append(new_row)

    @property
    def floor_count(self):
        floors = []
        for row in self.seats:
            for seat in row:
                if seat.floor:
                    floors.append((seat.row, seat.column))

        if floors == self.start_floors:
            return True

        return False

    @property
    def filled(self):
        total = 0
        for index in range(0, len(self.seats)):
            row = self.seats[index]
            # row_str = ''.join([i.printme() for i in row])
            new = len([i for i in row if i.filled])
            total += new

        return total

    def neighbors(self, row, column):
        matrix = [
            (row, column - 1),
            (row, column + 1),
            (row - 1, column),
            (row - 1, column - 1),
            (row - 1, column + 1),
            (row + 1, column),
            (row + 1, column - 1),
            (row + 1, column + 1),
        ]
        possible = [i for i in matrix if i[0] >= 0 and i[1] >= 0]
        neighbors = []
        for pair in possible:
            try:
                n = self.seats[pair[0]][pair[1]]
            except IndexError:
                continue
            neighbors.append(n)

        return neighbors

    def update(self):
        new_seats = []
        for rindex in range(0, len(self.seats)):
            row = self.seats[rindex]
            new_row = []
            for cindex in range(0, len(row)):
                seat = self.seats[rindex][cindex]
                if seat.floor:
                    new_row.append(seat)
                    continue

                ns = self.neighbors(rindex, cindex)
                occupied = len([i for i in ns if i.filled])
                new_seat = Seat(rindex, cindex)
                new_seat.filled = seat.filled
                if occupied >= 4:
                    new_seat.filled = False
                elif occupied == 0:
                    new_seat.filled = True
                new_row.append(new_seat)
            new_seats.append(new_row)

        self.seats = new_seats

    def printme(self):
        vis = []
        for row in self.seats:
            prow = []
            for seat in row:
                if seat.filled:
                    prow.append('#')
                elif seat.floor:
                    prow.append('.')
                else:
                    prow.append('L')
            vis.append(prow)

        return [''.join(i) for i in vis]


class Seat(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self._filled = False
        self.floor = False

    @property
    def filled(self):
        if self.floor:
            return False
        return self._filled

    @filled.setter
    def filled(self, value):
        if not self.floor:
            self._filled = value

    def printme(self):
        if self.filled:
            return '#'
        elif self.floor:
            return '.'
        else:
            return 'L'


if __name__ == '__main__':
    print(f'Test: {solve_test()}')
    print(f'Part1: {solve()}')
    print(f'Part2: {solve2()}')
