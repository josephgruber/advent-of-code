import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from lib.helper import (  # pylint: disable=import-error,no-name-in-module # NOQA: E402
    execution_timer,
    read_input,
)


@execution_timer
def solution(input: str, words_are_digits: bool = False):
    total_sum = 0
    digit_words = {
        "zero": "zero0zero",
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine",
    }

    for line in input.splitlines():
        if words_are_digits:
            for word, digit in digit_words.items():
                line = line.replace(word, digit)

        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        if first_digit is not None and last_digit is not None:
            total_sum += int(first_digit + last_digit)

    return total_sum


def main():
    puzzle_input = read_input("2023/1.txt")

    print(f"Part 1: {solution(input=puzzle_input, words_are_digits=False)}\n")
    print(f"Part 2: {solution(input=puzzle_input, words_are_digits=True)}")


if __name__ == "__main__":
    main()
