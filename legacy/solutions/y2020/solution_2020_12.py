import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import execution_timer, read_input, manhattan_distance  # pylint: disable=import-error,no-name-in-module,wrong-import-position # NOQA: E402,E501


def parse_instructions(data):
    instructions = {index: [instruction[0], int(instruction[1:])]
                    for index, instruction in enumerate(data.splitlines())}

    return instructions


def turn(direction, degrees, facing):
    cardinals = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}

    facing += degrees if direction == 'R' else (360 - degrees)
    facing %= 360

    direction = cardinals[facing]

    return (direction, facing)


def move(direction, units, location):
    loc_x, loc_y = location

    if direction == 'N':
        loc_y += units
    elif direction == 'S':
        loc_y -= units
    elif direction == 'E':
        loc_x += units
    elif direction == 'W':
        loc_x -= units

    return (loc_x, loc_y)


@execution_timer
def part1(data):
    instructions = parse_instructions(data)

    facing = ('E', 90)  # 0-3 = north, east, south, west
    ship_location = (0, 0)

    for instruction in instructions.items():
        action = instruction[1][0]
        value = instruction[1][1]

        if action == 'F':
            action = facing[0]

        if action in ['N', 'S', 'E', 'W']:
            ship_location = move(action, value, ship_location)
        elif action in ['L', 'R']:
            facing = turn(action, value, facing[1])

    distance = manhattan_distance((0, 0), ship_location)

    return distance


@execution_timer
def part2(data):
    instructions = parse_instructions(data)

    cardinals = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    ship_location = (0, 0)
    waypoint_location = (10, 1)

    for instruction in instructions.items():
        action = instruction[1][0]
        value = instruction[1][1]

        if action == 'F':
            ship_location = (ship_location[0] + (value * waypoint_location[0]),
                             ship_location[1] + (value * waypoint_location[1]))
        elif action in ['N', 'S', 'E', 'W']:
            waypoint_location = (waypoint_location[0] + (cardinals[action][0] * value),
                                 waypoint_location[1] + (cardinals[action][1] * value))
        elif action in ['L', 'R']:
            rot = (value if action == 'R' else (360 - value))

            if rot == 90:
                waypoint_location = (waypoint_location[1] * 1, waypoint_location[0] * -1)
            elif rot == 270:
                waypoint_location = (waypoint_location[1] * -1, waypoint_location[0] * 1)
            elif rot == 180:
                waypoint_location = (waypoint_location[0] * -1, waypoint_location[1] * -1)

    distance = manhattan_distance((0, 0), ship_location)

    return distance


def main():
    puzzle_input = read_input('2020_12.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
