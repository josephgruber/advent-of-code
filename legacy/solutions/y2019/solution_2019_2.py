import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from lib.helper import execution_timer, read_input


@execution_timer
def part1(intcode, inputs=None):
    opcodes = [int(code) for code in intcode.split(',')]

    if inputs:
        opcodes[1] = inputs[0]
        opcodes[2] = inputs[1]

    i = 0
    while opcodes[i] != 99:
        if opcodes[i] == 1:
            opcodes[opcodes[i + 3]] = opcodes[opcodes[i + 1]] + opcodes[opcodes[i + 2]]
        elif opcodes[i] == 2:
            opcodes[opcodes[i + 3]] = opcodes[opcodes[i + 1]] * opcodes[opcodes[i + 2]]

        i += 4

    return opcodes


@execution_timer
def part2(intcode, desired_output):
    for noun in range(100):
        for verb in range(100):
            if part1(intcode, [noun, verb])[0] == desired_output:
                return 100 * noun + verb

    return None


def main():
    puzzle_input = read_input('2019_2.txt')

    print(f'Part 1: {part1(puzzle_input, [12, 2])[0]}\n')
    print(f'Part 2: {part2(puzzle_input, 19690720)}')


if __name__ == '__main__':
    main()
