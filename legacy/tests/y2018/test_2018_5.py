import pytest
from solutions.y2018.solution_2018_5 import alchemicalReductionPart1, alchemicalReductionPart2

testData = [('aA', ''),
            ('abBA', ''),
            ('abAB', 'abAB'),
            ('aabAAB', 'aabAAB'),
            ('dabAcCaCBAcCcaDA', 'dabCBAcaDA')]


@pytest.mark.parametrize("input, expected", testData)
def test_day_5_part_1(input, expected):
  assert alchemicalReductionPart1(input) == expected


def test_day_5_part_2():
  testData = ('dabAcCaCBAcCcaDA', 'daDA')
  assert alchemicalReductionPart2(testData[0]) == testData[1]
