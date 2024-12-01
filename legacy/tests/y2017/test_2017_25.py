import pytest
from solutions.y2017.solution_2017_25 import theHaltingProblem


def test_day_25_part_1():
  testData = ({"A": [(1, 1, "B"), (0, -1, "B")], "B": [(1, -1, "A"), (1, 1, "A")]}, 6, 3)
  assert theHaltingProblem(testData[0], testData[1]) == testData[2]
