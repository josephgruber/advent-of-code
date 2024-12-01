import pytest
from solutions.y2020.solution_2020_5 import get_seat_id

TEST_INPUT_P1 = [('BFFFBBFRRR', 567), ('FFFBBBFRRR', 119), ('BBFFBBFRLL', 820), ('FBFBBFFRLR', 357)]


@pytest.mark.parametrize('test_input, expected_value', TEST_INPUT_P1)
def test_2020_5_1(test_input, expected_value):
    assert get_seat_id(test_input) == expected_value
