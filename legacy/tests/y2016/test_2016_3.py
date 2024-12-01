import pytest
from solutions.y2016.solution_2016_3 import part1, part2, isTriangle


def test_2016_3_1():
  input = '5 10 25'
  expected = 0
  assert part1(input) == expected


def test_2016_3_2():
  input = '''101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603'''
  expected = 6
  assert part2(input) == expected


testData_isTriangle = [([5, 10, 25], False), ([10, 20, 25], True)]
@pytest.mark.parametrize("input, expected", testData_isTriangle)
def test_2016_3_isTriangle(input, expected):
  assert isTriangle(input) == expected
