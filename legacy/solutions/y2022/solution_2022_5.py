import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import (  # pylint: disable=import-error,no-name-in-module # NOQA: E402
    execution_timer,
    read_input,
)


@execution_timer
def part1(data):
    procedure, stacks = process_stacks(data)

    for step in procedure:
        _, qty, _, src, _, dest = step.split()
        qty = int(qty)
        src = int(src)
        dest = int(dest)

        for _ in range(qty):
            stacks[dest - 1].insert(0, stacks[src - 1][0])
            stacks[src - 1].pop(0)

    return ''.join(crate[0] for crate in stacks)


@execution_timer
def part2(data):
    procedure, stacks = process_stacks(data)

    for step in procedure:
        _, qty, _, src, _, dest = step.split()
        qty = int(qty)
        src = int(src)
        dest = int(dest)

        stacks[dest - 1] = stacks[src - 1][:qty] + stacks[dest - 1]
        stacks[src - 1] = stacks[src - 1][qty:]

    return ''.join(crate[0] for crate in stacks)


def process_stacks(data):
    data = data.splitlines()

    idx = data.index('')  # look for the break between crate drawing and procedure list
    crates = data[:idx - 1]
    procedure = data[idx + 1:]

    crates = [[line[count * 4 + 1] for count in range(len(line) // 4 + 1)] for line in crates]
    stacks = [list(''.join(stack_column).strip()) for stack_column in zip(*crates)]

    return [procedure, stacks]


def main():
    puzzle_input = read_input('2022_5.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
