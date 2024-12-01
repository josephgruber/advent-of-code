import pytest
from solutions.y2016.solution_2016_1 import solution


testDataPart1 = [('R2, L3', 5), ('R2, R2, R2', 2), ('R5, L5, R5, R3', 12)]


@pytest.mark.parametrize("input, expected", testDataPart1)
def test_2016_1_1(input, expected):
  assert solution(input)[0] == expected


def test_2016_1_2():
  input = 'R8, R4, R4, R8'
  expected = 4
  assert solution(input)[1] == expected
