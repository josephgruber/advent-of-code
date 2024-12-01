from typing import List, Tuple

import pytest

from solutions.y2019.solution_2019_16 import part1, part2

TEST_DATA_P1: List[Tuple[str, str]] = [('80871224585914546619083218645595', '24176176'),
                                       ('19617804207202209144916044189917', '73745418'),
                                       ('69317163492948606335995924319873', '52432133')]

TEST_DATA_P2: List[Tuple[str, str]] = [('03036732577212944063491565474664', '84462026'),
                                       ('02935109699940807407585447034323', '78725270'),
                                       ('03081770884921959731165446850517', '53553731')]


@pytest.mark.parametrize('test_input, expected_value', TEST_DATA_P1)
def test_2019_16_1(test_input, expected_value):
  assert part1(test_input) == expected_value


@pytest.mark.parametrize('test_input, expected_value', TEST_DATA_P2)
def test_2019_16_2(test_input, expected_value):
  assert part2(test_input) == expected_value
