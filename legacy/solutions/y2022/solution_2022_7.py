import sys  # isort:skip
import os  # isort:skip

from collections import defaultdict

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import (  # pylint: disable=import-error,no-name-in-module # NOQA: E402
    execution_timer,
    read_input,
)


@execution_timer
def part1(terminal_output, max_size):
    filesystem = create_filesystem(terminal_output)

    return sum([size for size in filesystem.values() if size < max_size])


@ execution_timer
def part2(terminal_output, total_disk_space, required_free_disk_space):
    filesystem = create_filesystem(terminal_output)

    needed_space = required_free_disk_space - (total_disk_space - filesystem.get('/'))

    return [size for size in sorted(filesystem.values()) if size >= needed_space][0]


def create_filesystem(terminal_output):
    path = []
    tree = defaultdict(int)

    for output in terminal_output.splitlines():
        match output.split():
            case ['$', 'cd', directory]:
                if directory == '..':
                    path.pop()
                else:
                    path.append(directory)
            case ['$', 'ls']:
                continue
            case ['dir', directory]:
                continue
            case [size, _]:
                for idx in range(len(path)):
                    tree['/'.join(path[:idx + 1])] += int(size)
            case _:
                print(f'Unknown output: {output}')

    return tree


def main():
    puzzle_input = read_input('2022_7.txt')

    print(f'Part 1: {part1(puzzle_input, 100000)}\n')
    print(f'Part 2: {part2(puzzle_input, 70000000, 30000000)}')


if __name__ == '__main__':
    main()
