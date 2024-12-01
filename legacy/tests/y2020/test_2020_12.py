from solutions.y2020.solution_2020_12 import part1, part2

TEST_INPUT = """F10
N3
F7
R90
F11"""


def test_2020_12_1():
    expected_value = 25
    assert part1(TEST_INPUT) == expected_value


def test_2020_12_2():
    expected_value = 286
    assert part2(TEST_INPUT) == expected_value
