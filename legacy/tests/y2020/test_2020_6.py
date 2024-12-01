import pytest
from solutions.y2020.solution_2020_6 import part1, part2

TEST_INPUT = '''abc

a
b
c

ab
ac

a
a
a
a

b'''


def test_2020_6_1():
    expected_value = 11

    assert part1(TEST_INPUT) == expected_value


def test_2020_6_2():
    expected_value = 6

    assert part2(TEST_INPUT) == expected_value
