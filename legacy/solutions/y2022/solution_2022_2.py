import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import (  # pylint: disable=import-error,no-name-in-module # NOQA: E402
    execution_timer,
    read_input,
)


@execution_timer
def part1(guide):
    strategy_map = {'A X': 4, 'A Y': 8, 'A Z': 3,
                    'B X': 1, 'B Y': 5, 'B Z': 9,
                    'C X': 7, 'C Y': 2, 'C Z': 6}

    return sum(strategy_map[round] for round in guide.splitlines())


@execution_timer
def part2(guide):
    strategy_map = {'A X': 3, 'A Y': 4, 'A Z': 8,
                    'B X': 1, 'B Y': 5, 'B Z': 9,
                    'C X': 2, 'C Y': 6, 'C Z': 7}

    return sum(strategy_map[round] for round in guide.splitlines())


def main():
    puzzle_input = read_input('2022_2.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
