import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import execution_timer, read_input, int_list  # pylint: disable=import-error,no-name-in-module,wrong-import-position # NOQA: E402,E501


@execution_timer
def part1(data):
    adapters = [0] + sorted(int_list(data))
    adapters.append(max(adapters) + 3)

    differences = {3: 0, 2: 0, 1: 0}

    for index, adapter in enumerate(adapters[:-1]):
        differences[adapters[index + 1] - adapter] += 1

    jolt_difference = differences[1] * differences[3]

    return jolt_difference


@execution_timer
def part2(data):
    adapters = [0] + sorted(int_list(data))
    adapters.append(max(adapters) + 3)

    arrangements = [1] + adapters[-1] * [0]

    for adapter in adapters[1:]:
        arrangements[adapter] = arrangements[adapter - 3] + arrangements[adapter - 2] + arrangements[adapter - 1]

    return arrangements[-1]


def main():
    puzzle_input = read_input('2020_10.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
