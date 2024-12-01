import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from itertools import permutations

from lib.helper import execution_timer, read_input
from lib.intcode import Intcode


@execution_timer
def part1(program):
    thruster_signal = []

    for permutation in permutations(range(5)):
        input_signal = 0

        for phase_setting in permutation:
            computer = Intcode(program, [phase_setting, input_signal])
            output = list(computer.run())
            input_signal = output[-1]

        thruster_signal.append(input_signal)

    return max(thruster_signal)


@execution_timer
def part2(program):
    thruster_signal = []

    for permutation in permutations(range(5, 10)):
        i = 0

        amplifiers = [Intcode(program, [permutation[i]]) for i in range(5)]
        amplifiers[0].inputs.append(0)

        while amplifiers[4].halt is False:
            try:
                output = next(amplifiers[i].run())

                i = (i + 1) % 5

                amplifiers[i].inputs.append(output)
            except StopIteration:
                thruster_signal.append(output)
                break

    return max(thruster_signal)


def main():
    puzzle_input = read_input('2019_7.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
