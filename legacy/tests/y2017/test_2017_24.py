import pytest
from solutions.y2017.solution_2017_24 import electromagneticMoatPart1, electromagneticMoatPart2


# Part 1
def test_day_24_part_1():
  testData = ('''0/2
                2/2
                2/3
                3/4
                3/5
                0/1
                10/1
                9/10''', 31)
  assert electromagneticMoatPart1(testData[0]) == testData[1]


# Part 2
def test_day_24_part_2():
  testData = ('''0/2
                2/2
                2/3
                3/4
                3/5
                0/1
                10/1
                9/10''', 19)
  assert electromagneticMoatPart2(testData[0]) == testData[1]
