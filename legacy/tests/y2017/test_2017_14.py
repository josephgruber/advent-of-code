import pytest
from solutions.y2017.solution_2017_14 import diskDefragPart1, diskDefragPart2

# Part 1


def test_day_14_part_1():
  testData = ("flqrgnkx", 8108)
  assert diskDefragPart1(testData[0]) == testData[1]


# Part 2
def test_day_14_part_2():
  testData = ("flqrgnkx", 1242)
  assert diskDefragPart2(testData[0]) == testData[1]
