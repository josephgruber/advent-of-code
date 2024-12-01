import pytest

from solutions.y2022.solution_2022_6 import part1, part2

TEST_INPUT_P1 = [('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
                 ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
                 ('nppdvjthqldpwncqszvftbrmjlhg', 6),
                 ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
                 ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11)]

TEST_INPUT_P2 = [('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
                 ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
                 ('nppdvjthqldpwncqszvftbrmjlhg', 23),
                 ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
                 ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)]


@pytest.mark.parametrize('test_input, expected_value', TEST_INPUT_P1)
def test_2022_6_1(test_input, expected_value):
    assert part1(test_input) == expected_value


@pytest.mark.parametrize('test_input, expected_value', TEST_INPUT_P2)
def test_2022_6_2(test_input, expected_value):
    assert part2(test_input) == expected_value
