import pytest
from solutions.y2017.solution_2017_22 import sporificaVirusPart1, sporificaVirusPart2


# Part 1
def test_day_22_part_1():
  testData = ('''..#\n#..\n...''', 10000, 5587)
  assert sporificaVirusPart1(testData[0], testData[1]) == testData[2]


# Part 2
def test_day_22_part_2():
  testData = ("..#\n#..\n...", 100, 26)
  assert sporificaVirusPart2(testData[0], testData[1]) == testData[2]
