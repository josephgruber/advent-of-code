import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from itertools import accumulate
from typing import List

from lib.helper import execution_timer, read_input


@execution_timer
def part1(signal: str) -> str:
    input_signal: List[int] = [int(digit) for digit in signal]
    input_length: int = len(input_signal)
    output_signal: List[int] = []

    for _ in range(100):
        output_signal = [0] * input_length

        for digit in range(input_length):
            element: int = 0
            start: int = digit
            step: int = digit + 1

            while start < len(input_signal):
                element += sum(input_signal[start:start + step])
                start += 2 * step
                element -= sum(input_signal[start:start + step])
                start += 2 * step

            output_signal[digit] = abs(element) % 10

        input_signal = output_signal[:]

    return ''.join([str(char) for char in output_signal[:8]])


@execution_timer
def part2(signal: str) -> str:  # Leaned on AoC D16 thread for a hint on this solution
    signal = signal * 10000

    input_signal: List[int] = [int(digit) for digit in signal[int(signal[:7]):][::-1]]

    for _ in range(100):
        input_signal = list(accumulate(input_signal, lambda a, b: (a + b) % 10))

    return ''.join([str(char) for char in input_signal[::-1][:8]])


def main():
    puzzle_input = read_input('2019_16.txt').strip()

    result = part1(puzzle_input)
    print(f'Part 1: {result}\n')

    result = part2(puzzle_input)
    print(f'Part 2: {result}')


if __name__ == '__main__':
    main()
