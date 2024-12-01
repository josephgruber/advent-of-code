import pytest
from solutions.y2017.solution_2017_16 import permutationPromenadePart1


# Part 1
def test_day_16_part_1():
  testData = ("abcde", "s1,x3/4,pe/b", "baedc")
  assert permutationPromenadePart1(testData[0], testData[1]) == testData[2]
