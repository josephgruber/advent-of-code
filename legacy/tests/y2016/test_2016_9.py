import pytest
from solutions.y2016.solution_2016_9 import part1, part2

testData_part1 = [('ADVENT', 6), ('A(1x5)BC', 7), ('(3x3)XYZ', 9),
                  ('A(2x2)BCD(2x2)EFG', 11), ('(6x1)(1x3)A', 6), ('X(8x2)(3x3)ABCY', 18)]

testData_part2 = [('(3x3)XYZ', 9), ('X(8x2)(3x3)ABCY', 20), ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
                  ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445)]


@pytest.mark.parametrize("input, expected", testData_part1)
def test_2016_9_1(input, expected):
  assert part1(input) == expected


@pytest.mark.parametrize("input, expected", testData_part2)
def test_2016_9_2(input, expected):
  assert part2(input) == expected
