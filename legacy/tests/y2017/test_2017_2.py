import pytest
from solutions.y2017.solution_2017_2 import checksum_part1, checksum_part2


# Part 1
def test_day_2_part_1():
  testDataPart1 = [('''5 1 9 5
	7 5 3
	2 4 6 8''', 18)]

  assert checksum_part1(testDataPart1[0][0]) == testDataPart1[0][1]


# Part 2
def test_day_2_part_2():
  testDataPart2 = [('''5 9 2 8
	9 4 7 3
	3 8 6 5''', 9)]

  assert checksum_part2(testDataPart2[0][0]) == testDataPart2[0][1]
