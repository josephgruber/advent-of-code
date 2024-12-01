import pytest
from solutions.y2016.solution_2016_5 import solution


def test_2016_5_part_1():
  input = 'abc'
  expected = '18f47a30'
  assert solution(input) == expected


def test_2016_5_part_2():
  input = 'abc'
  expected = '05ace8e3'
  assert solution(input, position=True) == expected
