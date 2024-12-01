import pytest
from solutions.y2017.solution_2017_8 import processInstructionsPart1, processInstructionsPart2

# Part 1


def test_day_8_part_1():
  testDataPart1 = [('''b inc 5 if a > 1
    a inc 1 if b < 5
    c dec -10 if a >= 1
    c inc -20 if c == 10''', 1)]

  assert processInstructionsPart1(testDataPart1[0][0]) == testDataPart1[0][1]


# Part 2
def test_day_8_part_2():
  testDataPart2 = [('''b inc 5 if a > 1
    a inc 1 if b < 5
    c dec -10 if a >= 1
    c inc -20 if c == 10''', 10)]

  assert processInstructionsPart2(testDataPart2[0][0]) == testDataPart2[0][1]
