from solutions.y2022.solution_2022_3 import part1, part2

TEST_INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def test_2022_3_1():
    expected_value = 157

    assert part1(TEST_INPUT) == expected_value


def test_2022_3_2():
    expected_value = 70
    assert part2(TEST_INPUT) == expected_value
