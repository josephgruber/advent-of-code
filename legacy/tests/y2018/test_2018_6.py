import pytest
from solutions.y2018.solution_2018_6 import chronalCoordinates


def test_day_7_part_1():
  testData = ('''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9''', 17)
  assert chronalCoordinates(testData[0])[0] == testData[1]


def test_day_7_part_2():
  testData = ('''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9''', 32, 16)
  assert chronalCoordinates(testData[0], testData[1])[1] == testData[2]
