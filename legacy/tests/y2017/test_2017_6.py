import pytest
from solutions.y2017.solution_2017_6 import redistributionCyclesPart1, redistributionCyclesPart2


# Part 1
def test_day_6_part_1():
  testDataPart1 = [("0 2 7 0", 5)]

  assert redistributionCyclesPart1(testDataPart1[0][0]) == testDataPart1[0][1]


# Part 2
def test_day_6_part_2():
  testDataPart2 = [("0 2 7 0", 4)]

  assert redistributionCyclesPart2(testDataPart2[0][0]) == testDataPart2[0][1]
