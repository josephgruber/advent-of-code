import textwrap

from solutions.y2023.solution_2023_1 import solution


def test_2023_1_1():
    TEST_INPUT = """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
    """

    expected_value = 142
    assert solution(input=textwrap.dedent(TEST_INPUT).strip("/n"), words_are_digits=False) == expected_value


def test_2023_1_2():
    TEST_INPUT = """
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
    """

    expected_value = 281
    assert solution(input=textwrap.dedent(TEST_INPUT).strip("/n"), words_are_digits=True) == expected_value
