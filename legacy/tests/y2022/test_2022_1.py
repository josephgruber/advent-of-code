from solutions.y2022.solution_2022_1 import part1, part2

TEST_INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def test_2022_1_1():
    expected_value = 24000

    assert part1(TEST_INPUT) == expected_value


def test_2022_1_2():
    expected_value = 45000
    assert part2(TEST_INPUT) == expected_value
