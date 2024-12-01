import pytest
from solutions.y2016.solution_2016_2 import part1, part2


def test_2016_2_1():
  input = '''ULL
RRDDD
LURDL
UUUUD'''
  expected = 1985
  assert part1(input) == expected


def test_2016_2_2():
  input = '''ULL
RRDDD
LURDL
UUUUD'''
  expected = '5DB3'
  assert part2(input) == expected
