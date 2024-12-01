import pytest
from solutions.y2017.solution_2017_17 import spinLockPart1


# Part 1
def test_day_17_part_1():
  testData = (3, 638)
  assert spinLockPart1(testData[0]) == testData[1]
