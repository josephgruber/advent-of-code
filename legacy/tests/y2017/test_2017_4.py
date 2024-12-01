import pytest
from solutions.y2017.solution_2017_4 import validatePassphrasePart1, validatePassphrasePart2

# Part 1
testDataPart1 = [("aa bb cc dd ee", True),
                 ("aa bb cc dd aa", False),
                 ("aa bb cc dd aaa", True)]


@pytest.mark.parametrize("input, expected", testDataPart1)
def test_day_4_part_1(input, expected):
  assert validatePassphrasePart1(input) == expected


# Part 2
testDataPart2 = [("abcde fghij", True),
                 ("abcde xyz ecdab", False),
                 ("a ab abc abd abf abj", True),
                 ("iiii oiii ooii oooi oooo", True),
                 ("oiii ioii iioi iiio", False)]


@pytest.mark.parametrize("input, expected", testDataPart2)
def test_day_4_part_2(input, expected):
  assert validatePassphrasePart2(input) == expected
