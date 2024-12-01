import pytest
from solutions.y2015.solution_2015_1 import notQuiteLispPart1, notQuiteLispPart2


testDataPart1 = [('(())', 0),
                 ('()()', 0),
                 ('(((', 3),
                 ('(()(()(', 3),
                 ('))(((((', 3),
                 ('())', -1),
                 ('))(', -1),
                 (')))', -3),
                 (')())())', -3)]


@pytest.mark.parametrize("input, expected", testDataPart1)
def test_2015_1_1(input, expected):\
    assert notQuiteLispPart1(input) == expected


testDataPart2 = [(')', 1),
                 ('()())', 5)]


@pytest.mark.parametrize("input, expected", testDataPart2)
def test_2015_1_2(input, expected):\
    assert notQuiteLispPart2(input) == expected
