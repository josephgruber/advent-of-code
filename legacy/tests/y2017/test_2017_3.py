import pytest
from solutions.y2017.solution_2017_3 import manhattanDistance, spiralGridPart2


# Part 1
testDataPart1 = [(1, 0),
                 (12, 3),
                 (23, 2),
                 (1024, 31)]


@pytest.mark.parametrize("input, expected", testDataPart1)
def test_day_3_part_1(input, expected):
  assert manhattanDistance(input) == expected


# Part 2
testDataPart2 = [(27, 54),
                 (60, 122),
                 (300, 304),
                 (355, 362),
                 (700, 747),
                 (800, 806)]


@pytest.mark.parametrize("input, expected", testDataPart2)
def test_day_3_part_2(input, expected):
  assert spiralGridPart2(input) == expected
