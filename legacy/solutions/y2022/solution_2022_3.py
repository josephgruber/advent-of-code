import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import (  # pylint: disable=import-error,no-name-in-module # NOQA: E402
    execution_timer,
    read_input,
)


@execution_timer
def part1(rucksacks):
    priorities = 0

    for items in rucksacks.splitlines():
        compartment_size = len(items) // 2
        common_item = set(items[:compartment_size]).intersection(set(items[compartment_size:])).pop()
        priorities += (ord(common_item) - 38) if common_item.isupper() else (ord(common_item) - 96)

    return priorities


@ execution_timer
def part2(rucksacks):
    priorities = 0
    items = rucksacks.splitlines()

    for group in range(0, len(items), 3):
        common_item = set(items[group]).intersection(set(items[group + 1]), set(items[group + 2])).pop()
        priorities += (ord(common_item) - 38) if common_item.isupper() else (ord(common_item) - 96)

    return priorities


def main():
    puzzle_input = read_input('2022_3.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
