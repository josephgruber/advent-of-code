import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from functools import reduce
from itertools import combinations
from math import gcd

from lib.helper import execution_timer, read_input


@execution_timer
def part1(bodies, steps):
    state_vectors = parse(bodies)

    for _ in range(steps):
        state_vectors = propagate(state_vectors)

    total_energy = calc_energy(state_vectors)

    return sum(total_energy)


@execution_timer
def part2(bodies):
    first_state = dict()

    state_vectors = parse(bodies)

    first_state['x'] = [[val['pos'][0] for val in state_vectors.values()]]
    first_state['y'] = [[val['pos'][1] for val in state_vectors.values()]]
    first_state['z'] = [[val['pos'][2] for val in state_vectors.values()]]
    first_state['x'].append(None)
    first_state['y'].append(None)
    first_state['z'].append(None)

    step = 0

    while None in [val[1] for val in first_state.values()]:
        step += 1
        pos = []
        vel = []

        state_vectors = propagate(state_vectors)

        for i in range(3):
            pos.append([val['pos'][i] for val in state_vectors.values()])
            vel.append([val['vel'][i] for val in state_vectors.values()])

        if pos[0] == first_state['x'][0] and vel[0] == [0] * 4 and first_state['x'][1] is None:
            first_state['x'][1] = step

        if pos[1] == first_state['y'][0] and vel[1] == [0] * 4 and first_state['y'][1] is None:
            first_state['y'][1] = step

        if pos[2] == first_state['z'][0] and vel[2] == [0] * 4 and first_state['z'][1] is None:
            first_state['z'][1] = step

    return reduce(lambda a, b: a * b // gcd(a, b), [first_state['x'][1], first_state['y'][1], first_state['z'][1]])


def parse(bodies):
    state_vectors = dict()

    moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

    for moon, state_vector in enumerate(bodies.splitlines()):
        pos_x, pos_y, pos_z = state_vector[1:-1].split(', ')
        state_vectors[moons[moon]] = {'pos': [int(pos_x[2:]), int(pos_y[2:]), int(pos_z[2:])], 'vel': [0, 0, 0]}

    return state_vectors


def propagate(state_vectors):
    body_combinations = combinations(state_vectors, 2)

    for combination in body_combinations:
        state_vectors = update_gravity(state_vectors, combination)

    state_vectors = update_velocity(state_vectors)

    return state_vectors


def update_gravity(state_vectors, combination):
    for vector in range(3):
        if state_vectors[combination[0]]['pos'][vector] > state_vectors[combination[1]]['pos'][vector]:
            state_vectors[combination[0]]['vel'][vector] -= 1
            state_vectors[combination[1]]['vel'][vector] += 1
        elif state_vectors[combination[0]]['pos'][vector] < state_vectors[combination[1]]['pos'][vector]:
            state_vectors[combination[0]]['vel'][vector] += 1
            state_vectors[combination[1]]['vel'][vector] -= 1

    return state_vectors


def update_velocity(state_vectors):
    for body in state_vectors:
        for vector in range(3):
            state_vectors[body]['pos'][vector] += state_vectors[body]['vel'][vector]

    return state_vectors


def calc_energy(state_vectors):
    potential_energy = []
    kinetic_energy = []

    for body in state_vectors:
        potential_energy.append(sum(map(abs, state_vectors[body]['pos'])))
        kinetic_energy.append(sum(map(abs, state_vectors[body]['vel'])))

    return [potential_energy[i] * kinetic_energy[i] for i in range(len(potential_energy))]


def main():
    puzzle_input = read_input('2019_12.txt')

    print(f'Part 1: {part1(puzzle_input, 1000)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
