import sys  # isort:skip
import os

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import execution_timer, read_input  # pylint: disable=import-error,no-name-in-module,wrong-import-position # NOQA: E402,E501


@execution_timer
def solve(data, final_turn):
    numbers = [int(number) for number in data.split(',')]
    turn_spoken = {number: index for index, number in enumerate(numbers[:-1])}
    last_spoken = numbers[-1]

    for turn in range(len(numbers), final_turn):
        if last_spoken in turn_spoken:
            spoken_number = turn - turn_spoken[last_spoken] - 1
        else:
            spoken_number = 0

        turn_spoken[last_spoken] = turn - 1

        last_spoken = spoken_number

    return last_spoken


def main():
    puzzle_input = read_input('2020_15.txt')

    print(f'Part 1: {solve(puzzle_input, 2020)}\n')
    print(f'Part 2: {solve(puzzle_input, 30000000)}')


if __name__ == '__main__':
    main()
