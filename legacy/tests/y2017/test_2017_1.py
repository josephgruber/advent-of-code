import pytest
from solutions.y2017.solution_2017_1 import captcha_part1, captcha_part2


# Part 1
testDataPart1 = [("1122", 3),
                 ("1111", 4),
                 ("1234", 0),
                 ("91212129", 9)]


@pytest.mark.parametrize("input, expected", testDataPart1)
def test_day_1_part_1(input, expected):
  assert captcha_part1(input) == expected


# Part 2
testDataPart2 = [("1212", 6),
                 ("1221", 0),
                 ("123425", 4),
                 ("123123", 12),
                 ("12131415", 4)]


@pytest.mark.parametrize("input, expected", testDataPart2)
def test_day_1_part_2(input, expected):
  assert captcha_part2(input) == expected
