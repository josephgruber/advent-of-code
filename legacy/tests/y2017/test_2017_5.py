import pytest
from solutions.y2017.solution_2017_5 import findExitPart1, findExitPart2


# Part 1
def test_day_5_part_1():
  testDataPart1 = [('''0
	3
	0
	1
	-3''', 5)]

  assert findExitPart1(testDataPart1[0][0]) == testDataPart1[0][1]


# Part 2
def test_day_5_part_2():
  testDataPart2 = [('''0
	3
	0
	1
	-3''', 10)]

  assert findExitPart2(testDataPart2[0][0]) == testDataPart2[0][1]
