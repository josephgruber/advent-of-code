import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import (  # pylint: disable=import-error,no-name-in-module # NOQA: E402
    execution_timer,
    read_input,
)


@execution_timer
def part1(assignment_pairs):
    duplicates = 0

    for assignments in assignment_pairs.splitlines():
        sections = [int(section) for assignment in assignments.split(',') for section in assignment.split('-')]

        if (all(section_range in list(range(sections[0], sections[1] + 1))
                for section_range in list(range(sections[2], sections[3] + 1))) or
            all(section_range in list(range(sections[2], sections[3] + 1))
                for section_range in list(range(sections[0], sections[1] + 1)))):
            duplicates += 1

    return duplicates


@ execution_timer
def part2(assignment_pairs):
    duplicates = 0

    for assignments in assignment_pairs.splitlines():
        sections = [int(section) for assignment in assignments.split(',') for section in assignment.split('-')]

        if (any(section_range in list(range(sections[0], sections[1] + 1))
                for section_range in list(range(sections[2], sections[3] + 1)))):
            duplicates += 1

    return duplicates


def main():
    puzzle_input = read_input('2022_4.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
