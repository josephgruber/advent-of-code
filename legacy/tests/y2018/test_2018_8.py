import pytest
from solutions.y2018.solution_2018_8 import memoryManeuver


def test_day_8_part_1():
  testData = ('2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2', 138)
  assert sum(memoryManeuver(testData[0])[0]) == testData[1]


def test_day_8_part_2():
  testData = ('2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2', 66)
  assert memoryManeuver(testData[0])[1] == testData[1]
