import pytest
from solutions.y2015.solution_2015_10 import elvesLookElvesSay

testData = ['1', 5, 6]


def test_2015_10_1():
  assert elvesLookElvesSay(testData[0], testData[1]) == testData[2]
