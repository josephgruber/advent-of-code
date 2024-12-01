import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from copy import deepcopy  # NOQA: E402

from lib.helper import execution_timer, read_input  # pylint: disable=import-error,no-name-in-module,wrong-import-position # NOQA: E402,E501


@execution_timer
def part1(data):
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    memory = dict()

    for instruction in data.splitlines():
        address, value = instruction.split(' = ')

        if address == 'mask':
            mask = value
        else:
            bin_value = f'{int(value):036b}'

            for index, bit in enumerate(bin_value):
                if mask[index] in ('X', bit):
                    continue

                bin_value = bin_value[:index] + mask[index] + bin_value[index + 1:]

            memory[address[4:-1]] = int(bin_value, 2)

    return sum(memory.values())


@execution_timer
def part2(data):
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    memory = dict()

    for instruction in data.splitlines():
        address, value = instruction.split(' = ')

        if address == 'mask':
            mask = value
        else:
            bin_address = f'{int(address[4:-1]):036b}'
            bin_address_bits = []

            for index, bit in enumerate(bin_address):
                if mask[index] in ('X', bit):
                    bin_address_bits.append(mask[index])
                else:
                    bin_address_bits.append('1')

            bits = deepcopy(bin_address_bits)
            floats = bin_address_bits.count('X')

            for i in range(0, 2 ** floats):
                bins = bin(i)[2:].zfill(bin_address_bits.count('X'))

                for digit in bins:
                    bin_address_bits[bin_address_bits.index('X')] = digit

                memory[''.join(bin_address_bits)] = int(value)

                bin_address_bits = deepcopy(bits)

    return sum(memory.values())


def main():
    puzzle_input = read_input('2020_14.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
