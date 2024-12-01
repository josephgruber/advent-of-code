import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from re import search

from lib.helper import execution_timer


def is_password(password):
    if search(r'(\d)\1', password) and \
            password[0] <= password[1] <= password[2] <= password[3] <= password[4] <= password[5]:
        return True

    return False


def is_complex_password(password):
    character_count = [password.count(digit) for digit in set(password)]

    if 2 in character_count and \
            password[0] <= password[1] <= password[2] <= password[3] <= password[4] <= password[5]:
        return True

    return False


@execution_timer
def solution(password_range):
    begin, end = map(int, password_range.split('-'))

    valid_passwords = valid_complex_passwords = 0

    for password in range(begin, end + 1):
        valid_passwords += is_password(str(password))
        valid_complex_passwords += is_complex_password(str(password))

    return [valid_passwords, valid_complex_passwords]


def main():
    puzzle_input = '158126-624574'

    result = solution(puzzle_input)

    print(f'Part 1: {result[0]}\n')
    print(f'Part 2: {result[1]}')


if __name__ == '__main__':
    main()
