import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from lib.helper import execution_timer, read_input
from lib.intcode import Intcode


@execution_timer
def solution(intcode, inputs=None):
    computer = Intcode(intcode, inputs)
    output = list(computer.run())

    return output


def main():
    puzzle_input = read_input('2019_9.txt')

    print(f'Part 1: {solution(puzzle_input, [1])[0]}\n')
    print(f'Part 2: {solution(puzzle_input, [2])[0]}')


if __name__ == '__main__':
    main()
