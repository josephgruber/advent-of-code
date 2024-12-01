import pytest
from solutions.y2018.solution_2018_14 import chocolateChartsPart1, chocolateChartsPart2


# Part 1
testDataPart1 = [(9, '5158916779'),
                 (5, '0124515891'),
                 (18, '9251071085'),
                 (2018, '5941429882')]


@pytest.mark.parametrize("input, expected", testDataPart1)
def test_day_14_part_1(input, expected):
  assert chocolateChartsPart1(input) == expected

  # Part 1
testDataPart2 = [('51589', 9),
                 ('01245', 5),
                 ('92510', 18),
                 ('59414', 2018)]


@pytest.mark.parametrize("input, expected", testDataPart2)
def test_day_14_part_2(input, expected):
  assert chocolateChartsPart2(input) == expected
