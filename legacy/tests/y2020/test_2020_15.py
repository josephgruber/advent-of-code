import pytest
from solutions.y2020.solution_2020_15 import solve

TEST_INPUT_P1 = [('0,3,6', 436), ('1,3,2', 1), ('2,1,3', 10), ('1,2,3', 27),
                 ('2,3,1', 78), ('3,2,1', 438), ('3,1,2', 1836)]

TEST_INPUT_P2 = [('0,3,6', 175594), ('1,3,2', 2578), ('2,1,3', 3544142), ('1,2,3', 261214),
                 ('2,3,1', 6895259), ('3,2,1', 18), ('3,1,2', 362)]


@pytest.mark.parametrize('test_input, expected_value', TEST_INPUT_P1)
def test_2020_15_1(test_input, expected_value):
    assert solve(test_input, 2020) == expected_value


@pytest.mark.parametrize('test_input, expected_value', TEST_INPUT_P2)
def test_2020_15_2(test_input, expected_value):
    assert solve(test_input, 30000000) == expected_value
