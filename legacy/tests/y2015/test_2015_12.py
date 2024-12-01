import pytest
from solutions.y2015.solution_2015_12 import abacusFrameworkPart1, abacusFrameworkPart2


testDataPart1 = [('[1,2,3]', 6),
                 ('{"a":2,"b":4}', 6),
                 ('[[[3]]]', 3),
                 ('{"a":{"b":4},"c":-1}', 3),
                 ('{"a":[-1,1]}', 0),
                 ('[-1,{"a":1}]', 0),
                 ('[]', 0),
                 ('{}', 0)]


@pytest.mark.parametrize("input, expected", testDataPart1)
def test_2015_12_1(input, expected):
  assert abacusFrameworkPart1(input) == expected


testDataPart2 = [('[1, 2, 3]', 6),
                 ('[1,{"c":"red","b":2},3]', 4),
                 ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
                 ('[1,"red",5]', 6)]


@pytest.mark.parametrize("input, expected", testDataPart2)
def test_2015_12_2(input, expected):
  assert abacusFrameworkPart2(input) == expected
