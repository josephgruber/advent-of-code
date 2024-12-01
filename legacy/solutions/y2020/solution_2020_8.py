import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from copy import deepcopy  # NOQA: E402

from lib.helper import execution_timer, read_input  # pylint: disable=import-error,no-name-in-module,wrong-import-position # NOQA: E402,E501


def parse_instructions(boot_code):
    instructions = dict()

    for index, instruction in enumerate(boot_code.splitlines()):
        operation, argument = instruction.split(' ')
        instructions[index + 1] = dict(operation=operation, argument=int(argument), executed=False)

    return instructions


def run_program(instructions, part):
    accumulator = 0
    address = 1
    instructions_count = len(instructions) + 1

    while not instructions.get(address).get('executed'):
        operation = instructions.get(address).get('operation')
        argument = instructions.get(address).get('argument')

        instructions.get(address).update({'executed': True})

        if operation == 'nop':
            address = (address + 1) % instructions_count

        if operation == 'jmp':
            address = (address + argument) % instructions_count

        if operation == 'acc':
            address = (address + 1) % instructions_count
            accumulator += argument

        if not address:
            break

    if part == 1 or (part == 2 and not address):
        return accumulator

    return None


@execution_timer
def part1(data):
    instructions = parse_instructions(data)

    accumulator = run_program(instructions, 1)

    return accumulator


@execution_timer
def part2(data):
    accumulator = None
    instructions = parse_instructions(data)

    for instruction in instructions:
        operation = instructions[instruction]['operation']

        if operation in ['jmp', 'nop']:
            new_instructions = deepcopy(instructions)

            if operation == 'jmp':
                new_instructions[instruction]['operation'] = 'nop'
            else:
                new_instructions[instruction]['operation'] = 'jmp'

            accumulator = run_program(new_instructions, 2)

            if accumulator:
                break

    return accumulator


def main():
    puzzle_input = read_input('2020_8.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
