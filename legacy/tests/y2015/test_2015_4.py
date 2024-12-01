import pytest
from solutions.y2015.solution_2015_4 import stockingStuffer


testDataPart1 = [('abcdef', '00000', 609043), ('pqrstuv', '00000', 1048970)]


@pytest.mark.parametrize("key, search, expected", testDataPart1)
def test_2015_4_1(key, search, expected):
  assert stockingStuffer(key, search) == expected
