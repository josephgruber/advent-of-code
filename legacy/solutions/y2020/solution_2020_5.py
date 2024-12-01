import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import execution_timer, read_input  # pylint: disable=import-error,no-name-in-module # NOQA: E402


def get_seat_id(seat):
    seat = seat.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')

    return int(seat, 2)


@execution_timer
def get_all_seat_ids(data):
    seat_ids = set()

    for seat in data.splitlines():
        seat_ids.add(get_seat_id(seat))

    return seat_ids


@execution_timer
def get_missing_seat_id(data):
    seat_ids = get_all_seat_ids(data)

    missing_seat = list(set(range(min(seat_ids), max(seat_ids))) - seat_ids)

    return missing_seat[0]


def main():
    puzzle_input = read_input('2020_5.txt')

    print(f'Part 1: {max(get_all_seat_ids(puzzle_input))}\n')
    print(f'Part 2: {get_missing_seat_id(puzzle_input)}')


if __name__ == '__main__':
    main()
