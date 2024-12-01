import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from math import floor
from timeit import default_timer as timer

from lib.helper import execution_timer, read_input


@execution_timer
def solution(modules, include_fuel=False):
    total_fuel_required = 0

    for module in modules.splitlines():
        module_fuel = floor(int(module) / 3) - 2
        total_fuel_required += module_fuel

        if include_fuel:
            new_fuel = 0
            while module_fuel > 0:
                module_fuel = floor(module_fuel / 3) - 2
                if module_fuel > 0:
                    new_fuel += module_fuel

            total_fuel_required += new_fuel

    return total_fuel_required


def main():
    puzzle_input = read_input('2019_1.txt')

    print(f'Part 1: {solution(puzzle_input, False)}\n')
    print(f'Part 2: {solution(puzzle_input, True)}')


if __name__ == '__main__':
    main()
