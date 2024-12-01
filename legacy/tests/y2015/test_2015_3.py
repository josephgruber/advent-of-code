import pytest
from solutions.y2015.solution_2015_3 import sphericalHouses


testDataPart1 = [('>', 2), ('^>v<', 4), ('^v^v^v^v^v', 2)]


@pytest.mark.parametrize("input, expected", testDataPart1)
def test_2015_3_1(input, expected):
  assert sphericalHouses(input)[0] == expected


testDataPart2 = [('^v', 3), ('^>v<', 3), ('^v^v^v^v^v', 11)]


@pytest.mark.parametrize("input, expected", testDataPart2)
def test_2015_3_2(input, expected):
  assert sphericalHouses(input)[1] == expected
