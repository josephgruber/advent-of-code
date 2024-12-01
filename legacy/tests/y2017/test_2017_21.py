import pytest
from solutions.y2017.solution_2017_21 import fractalArt


# Part 1
def test_day_21_part_1():
  testData = ('''../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#''', 2, 12)
  assert fractalArt(testData[0], testData[1]) == testData[2]

# Part 2


def test_day_21_part_2():
  testData = ('''../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#''', 2, 12)
  assert fractalArt(testData[0], testData[1]) == testData[2]
