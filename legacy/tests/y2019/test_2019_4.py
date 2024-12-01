import pytest
from solutions.y2019.solution_2019_4 import is_password, is_complex_password

TEST_DATA_P1 = [('111111', True), ('223450', False), ('123789', False)]

TEST_DATA_P2 = [('112233', True), ('123444', False), ('111122', True)]


@pytest.mark.parametrize('test_input, expected_value', TEST_DATA_P1)
def test_2019_4_1(test_input, expected_value):
  assert is_password(test_input) == expected_value


@pytest.mark.parametrize('test_input, expected_value', TEST_DATA_P2)
def test_2019_4_2(test_input, expected_value):
  assert is_complex_password(test_input) == expected_value
