import pytest
from solutions.y2018.solution_2018_3 import fabricClaimsPart1, fabricClaimsPart2


# Part 1
def test_day_3_part_1():
  testData = ('''#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2''', 4)
  assert fabricClaimsPart1(testData[0]) == testData[1]


def test_day_3_part_2():
  testData = ('''#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2''', 3)
  assert fabricClaimsPart2(testData[0]) == testData[1]
