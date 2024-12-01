import pytest
from solutions.y2019.solution_2019_9 import solution

TEST_DATA_P1 = [('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99', None,
                 [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]),
                ('1102,34915192,34915192,7,4,7,99,0', None, [1219070632396864]),
                ('104,1125899906842624,99', None, [1125899906842624])]


@pytest.mark.parametrize('test_input, param1, expected_value', TEST_DATA_P1)
def test_2019_9_1(test_input, param1, expected_value):
  assert solution(test_input, [param1]) == expected_value
