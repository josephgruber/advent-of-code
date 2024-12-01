import pytest
from solutions.y2017.solution_2017_13 import packetScannerPart1, packetScannerPart2


# Part 1
def test_day_13_part_1():
  testData = ('''0: 3
                1: 2
                4: 4
                6: 4''', 24)
  assert packetScannerPart1(testData[0]) == testData[1]


# Part 2
def test_day_13_part_2():
  testData = ('''0: 3
                1: 2
                4: 4
                6: 4''', 10)
  assert packetScannerPart2(testData[0]) == testData[1]
