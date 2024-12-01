from solutions.y2020.solution_2020_8 import part1, part2

TEST_INPUT = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def test_2020_8_1():
    expected_value = 5

    assert part1(TEST_INPUT) == expected_value


def test_2020_8_2():
    expected_value = 8

    assert part2(TEST_INPUT) == expected_value
