import pytest
from solutions.y2017.solution_2017_10 import knotHashPart1


def test_day_10_part_1():
  testData = ((3, 4, 1, 5), 5, 12)
  assert knotHashPart1(testData[0], testData[1]) == testData[2]
