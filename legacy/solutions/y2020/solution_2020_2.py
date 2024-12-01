import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import execution_timer, read_input  # pylint: disable=import-error,no-name-in-module # NOQA: E402


@execution_timer
def part1(password_list):
    valid_passwords = 0

    for policy in password_list.splitlines():
        strength, letter, password = policy.split()
        min_strength, max_strength = [int(value) for value in strength.split('-')]
        letter = letter[:-1]

        if password.count(letter) in range(min_strength, max_strength + 1):
            valid_passwords += 1

    return valid_passwords


@execution_timer
def part2(password_list):
    valid_passwords = 0

    for policy in password_list.splitlines():
        positions, letter, password = policy.split()
        pos1, pos2 = [int(value) for value in positions.split('-')]
        letter = letter[:-1]

        if (password[pos1 - 1], password[pos2 - 1]).count(letter) == 1:
            valid_passwords += 1

    return valid_passwords


def main():
    puzzle_input = read_input('2020_2.txt')

    print(f'Part 1: {part1(puzzle_input)}\n')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == '__main__':
    main()
