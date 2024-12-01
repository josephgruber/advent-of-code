import pytest
from solutions.y2016.solution_2016_6 import solution

input = '''eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar'''


def test_2016_6_part_1():
  expected = 'easter'
  assert solution(input)[0] == expected


def test_2016_6_part_2():
  expected = 'advent'
  assert solution(input)[1] == expected
