import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from copy import deepcopy  # NOQA: E402
from collections import Counter  # NOQA: E402

from lib.helper import execution_timer, read_input  # pylint: disable=import-error,no-name-in-module,wrong-import-position # NOQA: E402,E501


def is_occupied_p1(grid, location):
    adjacent_occupied = 0
    loc_x = location[0]
    loc_y = location[1]

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dir_x, dir_y in directions:
        if grid.get((loc_x + dir_x, loc_y + dir_y)) == '#':
            adjacent_occupied += 1

        if adjacent_occupied >= 4:
            break

    return adjacent_occupied


def is_occupied_p2(grid, location):
    adjacent_occupied = 0
    max_x, max_y = max(grid)
    loc_x = location[0]
    loc_y = location[1]

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dir_x, dir_y in directions:
        seat_x = loc_x + dir_x
        seat_y = loc_y + dir_y

        while 0 <= seat_x <= max_x and 0 <= seat_y <= max_y:
            seat = grid.get((seat_x, seat_y))
            if seat == '#':
                adjacent_occupied += 1
                break

            if seat == 'L':
                break

            seat_x += dir_x
            seat_y += dir_y

        if adjacent_occupied >= 5:
            break

    return adjacent_occupied


@execution_timer
def part1(data):
    grid = {(x, y): cell for y, row in enumerate(data.splitlines()) for x, cell in enumerate(row)}
    new_grid = None

    while True:
        new_grid = deepcopy(grid)

        for position in grid:
            position_type = grid.get(position)

            if position_type == '.':
                continue

            if position_type == '#' and is_occupied_p1(grid=grid, location=position) >= 4:
                new_grid[position] = 'L'
            elif position_type == 'L' and not is_occupied_p1(grid=grid, location=position):
                new_grid[position] = '#'

        if new_grid == grid:
            break

        grid = new_grid

    empty_seats = Counter(grid.values())['#']

    return empty_seats


@execution_timer
def part2(data):
    grid = {(x, y): cell for y, row in enumerate(data.splitlines()) for x, cell in enumerate(row)}
    new_grid = None

    while True:
        new_grid = deepcopy(grid)

        for position in grid:
            position_type = grid.get(position)

            if position_type == '.':
                continue

            if position_type == '#' and is_occupied_p2(grid=grid, location=position) >= 5:
                new_grid[position] = 'L'
            elif position_type == 'L' and not is_occupied_p2(grid=grid, location=position):
                new_grid[position] = '#'

        if new_grid == grid:
            break

        grid = new_grid

    empty_seats = Counter(grid.values())['#']

    return empty_seats


def main():
    puzzle_input = read_input('2020_11.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
