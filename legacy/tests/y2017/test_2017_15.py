import pytest

from solutions.y2017.solution_2017_15 import (
    duelingGeneratorPart1,
    duelingGeneratorPart2,
)


# Part 1
@pytest.mark.skip(reason="takes too long")
def test_day_15_part_1():
  testData = (65, 8921, 588)
  assert duelingGeneratorPart1(testData[0], testData[1]) == testData[2]


# Part 2
@pytest.mark.skip(reason="takes too long")
def test_day_15_part_2():
  testData = (65, 8921, 4, 8, 309)
  assert duelingGeneratorPart2(testData[0], testData[1], testData[2], testData[3]) == testData[4]
