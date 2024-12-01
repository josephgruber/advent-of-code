import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

import re
from timeit import default_timer as timer

import numpy

from lib.helper import read_input


def fireHazardPart1(instructions):
    grid = numpy.zeros((1000, 1000), dtype=numpy.bool_)

    for instruction in instructions.splitlines():
        steps = re.findall(
            r'(turn on|turn off|toggle)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)', instruction.strip())

        operation = steps[0][0]
        startX = int(steps[0][1])
        startY = int(steps[0][2])
        endX = int(steps[0][3]) + 1
        endY = int(steps[0][4]) + 1

        if operation == 'toggle':
            grid[slice(startX, endX), slice(startY, endY)] ^= numpy.True_
        else:
            grid[slice(startX, endX), slice(startY, endY)] = {
                'turn on': numpy.True_, 'turn off': numpy.False_}[operation]

    return grid[grid == numpy.True_].sum()


def fireHazardPart2(instructions):
    grid = numpy.zeros((1000, 1000), dtype=int)

    for instruction in instructions.splitlines():
        steps = re.findall(
            r'(turn on|turn off|toggle)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)', instruction.strip())

        operation = steps[0][0]
        startX = int(steps[0][1])
        startY = int(steps[0][2])
        endX = int(steps[0][3]) + 1
        endY = int(steps[0][4]) + 1

        grid[slice(startX, endX), slice(startY, endY)] += {'toggle': 2, 'turn on': 1, 'turn off': -1}[operation]
        grid[grid < 0] = 0

    return grid.sum()


def main():
    data = read_input("2015_6.txt")

    start_time = timer()
    print('Part 1: ' + str(fireHazardPart1(data)))
    end_time = timer()
    print('Elapsed Time: ' + str(end_time - start_time))
    print()

    start_time = timer()
    print('Part 2: ' + str(fireHazardPart2(data)))
    end_time = timer()
    print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
    main()
