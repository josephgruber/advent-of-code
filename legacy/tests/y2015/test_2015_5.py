import pytest
from solutions.y2015.solution_2015_5 import part1, part2


testDataPart1 = [('ugknbfddgicrmopn', True),
                 ('aaa', True),
                 ('jchzalrnumimnmhp', False),
                 ('haegwjzuvuyypxyu', False),
                 ('dvszwmarrgswjxmb', False)]


@pytest.mark.parametrize("input, expected", testDataPart1)
def test_2015_5_1(input, expected):
  assert part1(input) == expected


testDataPart2 = [('qjhvhtzxzqqjkmpb', True),
                 ('xxyxx', True),
                 ('uurcxstgmygtbstg', False),
                 ('ieodomkazucvgmuy', False)]


@pytest.mark.parametrize("input, expected", testDataPart2)
def test_2015_5_2(input, expected):
  assert part2(input) == expected
