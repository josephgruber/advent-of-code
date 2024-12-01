import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import (  # pylint: disable=import-error,no-name-in-module # NOQA: E402
    execution_timer,
    read_input,
)


@execution_timer
def part1(stream):
    marker = find_stream_marker(stream, 4)

    return marker


@execution_timer
def part2(stream):
    marker = find_stream_marker(stream, 14)

    return marker


def find_stream_marker(stream, chars):
    for idx in range(len(stream) - chars):
        if len(set(stream[idx:idx + chars])) == chars:
            return idx + chars

    return None


def main():
    puzzle_input = read_input('2022_6.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
