import pytest
from solutions.y2017.solution_2017_11 import hexEdPart1, hexEdPart2


# Part 1
testData = [("ne, ne, ne", 3),
            ("ne, ne, sw, sw", 0),
            ("ne, ne, s, s", 2),
            ("se, sw, se, sw, sw", 3)]


@pytest.mark.parametrize("input, expected", testData)
def test_day_11_part_1(input, expected):
  assert hexEdPart1(input) == expected


# Part 2
testData = [("ne, ne, ne", 3),
            ("ne,ne,sw,sw", 2),
            ("ne, ne, s, s", 2),
            ("se, sw, se, sw, sw", 3)]


@pytest.mark.parametrize("input, expected", testData)
def test_day_11_part_2(input, expected):
  assert hexEdPart2(input) == expected
