import pytest
from solutions.y2019.solution_2019_2 import part1

TEST_DATA_P1 = [('1,9,10,3,2,3,11,0,99,30,40,50', [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]),
                ('1,0,0,0,99', [2, 0, 0, 0, 99]), ('2,3,0,3,99', [2, 3, 0, 6, 99]),
                ('2,4,4,5,99,0', [2, 4, 4, 5, 99, 9801]), ('1,1,1,4,99,5,6,0,99', [30, 1, 1, 4, 2, 5, 6, 0, 99])]


@pytest.mark.parametrize('test_input, expected_value', TEST_DATA_P1)
def test_2019_2_1(test_input, expected_value):
  assert part1(test_input) == expected_value
