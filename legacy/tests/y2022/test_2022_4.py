from solutions.y2022.solution_2022_4 import part1, part2

TEST_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def test_2022_4_1():
    expected_value = 2

    assert part1(TEST_INPUT) == expected_value


def test_2022_4_2():
    expected_value = 4
    assert part2(TEST_INPUT) == expected_value
