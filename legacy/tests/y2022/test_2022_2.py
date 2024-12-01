from solutions.y2022.solution_2022_2 import part1, part2

TEST_INPUT = """A Y
B X
C Z"""


def test_2022_2_1():
    expected_value = 15

    assert part1(TEST_INPUT) == expected_value


def test_2022_2_2():
    expected_value = 12
    assert part2(TEST_INPUT) == expected_value
