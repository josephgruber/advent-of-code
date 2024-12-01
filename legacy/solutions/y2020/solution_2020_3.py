import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from math import prod  # NOQA: E402

from lib.helper import execution_timer, read_input  # pylint: disable=import-error,no-name-in-module # NOQA: E402


@execution_timer
def check_slope(data, slope):
    trees = 0
    y = 0

    forest = [list(line) for line in data.splitlines()]
    for row in range(0, len(forest), slope[1]):
        if forest[row][y] == '#':
            trees += 1

        y = (y + slope[0]) % len(forest[0])

    return trees


@execution_timer
def all_slopes(data, slopes):
    product_of_trees = prod([check_slope(data, slope) for slope in slopes])

    return product_of_trees


def main():
    puzzle_input = read_input('2020_3.txt')

    print(f'Part 1: {check_slope(puzzle_input, (3, 1))}\n')

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(f'Part 2: {all_slopes(puzzle_input, slopes)}')


if __name__ == '__main__':
    main()
