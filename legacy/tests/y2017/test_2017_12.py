import pytest
from solutions.y2017.solution_2017_12 import digitalPlumberPart1, digitalPlumberPart2


# Part 1
def test_day_12_part_1():
  testData = ('''0 <-> 2
				1 <-> 1
				2 <-> 0, 3, 4
				3 <-> 2, 4
				4 <-> 2, 3, 6
				5 <-> 6
				6 <-> 4, 5''', 6)
  assert digitalPlumberPart1(testData[0]) == testData[1]


# Part 2
def test_day_12_part_2():
  testData = ('''0 <-> 2
				1 <-> 1
				2 <-> 0, 3, 4
				3 <-> 2, 4
				4 <-> 2, 3, 6
				5 <-> 6
				6 <-> 4, 5''', 2)
  assert digitalPlumberPart2(testData[0]) == testData[1]
