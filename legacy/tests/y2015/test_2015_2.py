import pytest
from solutions.y2015.solution_2015_2 import wrappingPaper


testDataPart1 = [('2x3x4', 58),
                 ('1x1x10', 43)]


@pytest.mark.parametrize("input, expected", testDataPart1)
def test_2015_2_1(input, expected):\
    assert wrappingPaper(input)[0] == expected


testDataPart2 = [('2x3x4', 34),
                 ('1x1x10', 14)]


@pytest.mark.parametrize("input, expected", testDataPart2)
def test_2015_2_2(input, expected):\
    assert wrappingPaper(input)[1] == expected
