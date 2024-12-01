import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from itertools import combinations  # NOQA: E402

from lib.helper import execution_timer, read_input, int_list  # pylint: disable=import-error,no-name-in-module,wrong-import-position # NOQA: E402,E501


@execution_timer
def part1(data, preamble_length):
    value = None
    data = int_list(data)

    for index, value in enumerate(data[preamble_length:]):
        preamble = data[index:index + preamble_length]

        if value not in [sum(combo) for combo in combinations(preamble, 2)]:
            break

    return value


@execution_timer
def part2(data, target):
    low = 0
    high = 1

    data = int_list(data)

    invalid_sum = sum(data[low:high])

    while invalid_sum != target:
        if invalid_sum < target:
            high += 1
        else:
            low += 1

        invalid_sum = sum(data[low:high])

    weakness = min(data[low:high]) + max(data[low:high])

    return weakness


def main():
    puzzle_input = read_input('2020_9.txt')

    part1_answer = part1(puzzle_input, preamble_length=25)
    print(f'Part 1: {part1_answer}\n')
    print(f'Part 2: {part2(puzzle_input, target=part1_answer)}')


if __name__ == '__main__':
    main()
