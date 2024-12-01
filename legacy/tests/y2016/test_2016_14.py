import pytest

from solutions.y2016.solution_2016_14 import solution


def test_2016_14_1():
  test_input = 'abc'
  expected = 22728
  puzzle = 1

  assert solution(test_input, puzzle) == expected

@pytest.mark.skip(reason="takes too long")
def test_2016_14_2():
  test_input = 'abc'
  expected = 22551
  puzzle = 2

  assert solution(test_input, puzzle) == expected
