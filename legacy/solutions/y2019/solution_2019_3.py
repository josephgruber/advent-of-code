import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from lib.helper import execution_timer, manhattan_distance, read_input


@execution_timer
def solution(wires):
    def trace(wire):
        position = [0, 0]
        path = set()
        path_steps = dict()
        steps = 1

        for turn in wire.split(','):
            for _ in range(int(turn[1:])):
                if turn[0] == 'R':
                    position[0] += 1
                elif turn[0] == 'U':
                    position[1] += 1
                elif turn[0] == 'L':
                    position[0] -= 1
                elif turn[0] == 'D':
                    position[1] -= 1

                if tuple(position) not in path_steps:
                    path_steps[tuple(position)] = steps

                path.add(tuple(position))

                steps += 1

        return [path, path_steps]

    wire_a, wire_b = wires.splitlines()
    distances, common_steps = [], []

    wire_a_path, wire_a_path_steps = trace(wire_a)
    wire_b_path, wire_b_path_steps = trace(wire_b)

    for intersection in wire_a_path.intersection(wire_b_path):
        common_steps.append(wire_a_path_steps[intersection] + wire_b_path_steps[intersection])
        distances.append(manhattan_distance((0, 0), intersection))

    return [min(distances), min(common_steps)]


def main():
    puzzle_input = read_input('2019_3.txt')

    print(f'Part 1: {solution(puzzle_input)[0]}\n')
    print(f'Part 2: {solution(puzzle_input)[1]}')


if __name__ == '__main__':
    main()
