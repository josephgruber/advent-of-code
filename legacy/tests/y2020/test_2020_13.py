import pytest

from solutions.y2020.solution_2020_13 import part1, part2

TEST_INPUT_P1 = [("""939\n7,13,x,x,59,x,31,19""", 295)]

TEST_INPUT_P2 = [("""939\n17,x,13,19""", 3417),
                 ("""939\n67,7,59,61""", 754018),
                 ("""939\n67,x,7,59,61""", 779210),
                 ("""939\n67,7,x,59,61""", 1261476),
                 ("""939\n1789,37,47,1889""", 1202161486)]


@pytest.mark.parametrize('test_input, expected_value', TEST_INPUT_P1)
def test_2020_13_1(test_input, expected_value):
    assert part1(test_input) == expected_value


@pytest.mark.parametrize('test_input, expected_value', TEST_INPUT_P2)
def test_2020_13_2(test_input, expected_value):
    assert part2(test_input) == expected_value
