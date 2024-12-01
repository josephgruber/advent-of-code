import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import (  # pylint: disable=import-error,no-name-in-module # NOQA: E402
    execution_timer,
    read_input,
)


@execution_timer
def part1(inventory):
    return max([sum([int(food) for food in i]) for i in [elf.split('\n') for elf in inventory.split('\n\n')]])


@execution_timer
def part2(inventory):
    return sum(sorted([sum([int(food) for food in i]) for i in [elf.split('\n') for elf in inventory.split('\n\n')]])[-3:])


def main():
    puzzle_input = read_input('2022_1.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
