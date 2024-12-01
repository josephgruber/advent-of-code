import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

import networkx as nx

from lib.helper import execution_timer, read_input


@execution_timer
def part_1(local_orbits):
    total_orbits = 0

    graph = create_orbit_map(local_orbits)

    for orbits in graph.nodes:
        total_orbits += nx.shortest_path_length(graph, orbits, 'COM')

    return total_orbits


@execution_timer
def part_2(local_orbits, object_a, object_b):
    graph = create_orbit_map(local_orbits)

    return nx.shortest_path_length(graph, object_a, object_b) - 2


def create_orbit_map(local_orbits):
    graph = nx.Graph()

    for orbits in local_orbits.splitlines():
        graph.add_edge(*orbits.split(')'))

    return graph


def main():
    puzzle_input = read_input('2019_6.txt')

    print(f'Part 1: {part_1(puzzle_input)}\n')
    print(f'Part 2: {part_2(puzzle_input, "YOU", "SAN")}')


if __name__ == '__main__':
    main()
