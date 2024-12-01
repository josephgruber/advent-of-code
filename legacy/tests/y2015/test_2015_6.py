import pytest
from solutions.y2015.solution_2015_6 import fireHazardPart1, fireHazardPart2


testDataPart1 = [('turn on 0,0 through 999,999', 1000000),
                 ('toggle 0,0 through 999,0', 1000),
                 ('turn off 499,499 through 500,500', 0)]


@pytest.mark.parametrize("input, expected", testDataPart1)
def test_2015_6_1(input, expected):
  assert fireHazardPart1(input) == expected


testDataPart2 = [('turn on 0,0 through 0,0', 1),
                 ('toggle 0,0 through 999,999', 2000000)]


@pytest.mark.parametrize("input, expected", testDataPart2)
def test_2015_6_2(input, expected):
  assert fireHazardPart2(input) == expected
