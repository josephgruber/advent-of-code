import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from itertools import combinations  # NOQA: E402

from lib.helper import execution_timer, read_input, int_list  # pylint: disable=import-error,no-name-in-module # NOQA: E402


@execution_timer
def part1(expense_report):
    expenses = int_list(expense_report)

    for expense in expenses:
        if 2020 - expense in expenses:
            return expense * (2020 - expense)

    return 0


@execution_timer
def part2(expense_report):
    expenses = int_list(expense_report)

    for x, y, z in combinations(expenses, 3):
        if x + y + z == 2020:
            return x * y * z

    return 0


def main():
    puzzle_input = read_input('2020_1.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
