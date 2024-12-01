import pytest
from solutions.y2016.solution_2016_8 import solution


def test_2016_8_1():
  input = '''rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1'''
  expected = 6
  assert solution(input) == expected
