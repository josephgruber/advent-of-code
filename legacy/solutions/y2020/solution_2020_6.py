import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import execution_timer, read_input  # pylint: disable=import-error,no-name-in-module # NOQA: E402


@execution_timer
def part1(data):
    return sum([len(set(group.replace('\n', ''))) for group in data.split('\n\n')])


@execution_timer
def part2(data):
    return sum([len(set.intersection(*[set(person) for person in group.split('\n')])) for group in data.split('\n\n')])


def main():
    puzzle_input = read_input('2020_6.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
