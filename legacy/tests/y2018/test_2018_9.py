import pytest
from solutions.y2018.solution_2018_9 import marbleMania


# Part 1
testDataPart1 = [('9, 25', 32),
                 ('10, 1618', 8317),
                 ('13, 7999', 146373),
                 ('17, 1104', 2764),
                 ('21, 6111', 54718),
                 ('30, 5807', 37305)]


@pytest.mark.parametrize("input, expected", testDataPart1)
def test_day_9_part_1(input, expected):
  players, lastMarble = map(int, input.strip().split(', '))
  assert marbleMania(players, lastMarble) == expected
