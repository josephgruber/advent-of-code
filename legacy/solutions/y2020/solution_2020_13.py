import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import (  # pylint: disable=import-error,no-name-in-module,wrong-import-position # NOQA: E402,E501
    execution_timer,
    read_input,
)


def parse_data(data):
    data = data.split('\n')

    timestamp = int(data[0])
    bus_ids = [int(value) for value in data[1].split(',') if value != 'x']

    return (timestamp, bus_ids)


@execution_timer
def part1(data):
    notes = parse_data(data)
    schedule = {}

    for bus in notes[1]:
        schedule[bus] = (notes[0] + bus) - notes[0] % bus

    next_bus = min(schedule, key=schedule.get)

    answer = next_bus * (schedule[next_bus] - notes[0])

    return answer


@execution_timer
def part2(data):
    notes = data.splitlines()[1].split(',')
    buses = [(index, int(bus_id)) for index, bus_id in enumerate(notes) if bus_id != 'x']

    timestamp = 0
    step = 1

    for index, bus_id in buses:
        while (timestamp + index) % bus_id:
            timestamp += step

        step *= bus_id

    return timestamp


def main():
    puzzle_input = read_input('2020_13.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
