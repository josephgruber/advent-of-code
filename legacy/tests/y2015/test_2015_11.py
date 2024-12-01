import pytest
from solutions.y2015.solution_2015_11 import isValidPassword, corporatePolicy


testDataPart1A = [('hijklmmn', False),
                  ('abbceffg', False),
                  ('abbcegjk', False),
                  ('abcdffaa', True),
                  ('ghjaabcc', True)]


@pytest.mark.parametrize("input, expected", testDataPart1A)
def test_2015_12_1A(input, expected):
  assert isValidPassword(input) == expected


testDataPart1B = [('abcdefgh', 'abcdffaa')]


@pytest.mark.parametrize("input, expected", testDataPart1B)
def test_2015_12_1B(input, expected):
  assert corporatePolicy(input) == expected
