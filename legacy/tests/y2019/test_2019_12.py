import pytest
from solutions.y2019.solution_2019_12 import part1, part2

TEST_DATA_P1 = [('<x=-1, y=0, z=2>\n<x=2, y=-10, z=-7>\n<x=4, y=-8, z=8>\n<x=3, y=5, z=-1>', 10, 179),
                ('<x=-8, y=-10, z=0>\n<x=5, y=5, z=10>\n<x=2, y=-7, z=3>\n<x=9, y=-8, z=-3>', 100, 1940)]

TEST_DATA_P2 = [('<x=-1, y=0, z=2>\n<x=2, y=-10, z=-7>\n<x=4, y=-8, z=8>\n<x=3, y=5, z=-1>', 2772),
                ('<x=-8, y=-10, z=0>\n<x=5, y=5, z=10>\n<x=2, y=-7, z=3>\n<x=9, y=-8, z=-3>', 4686774924)]


@pytest.mark.parametrize('test_input, param1, expected_value', TEST_DATA_P1)
def test_2019_12_1(test_input, param1, expected_value):
  assert part1(test_input, param1) == expected_value


@pytest.mark.parametrize('test_input, expected_value', TEST_DATA_P2)
def test_2019_12_2(test_input, expected_value):
  assert part2(test_input) == expected_value
