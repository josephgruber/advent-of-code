import pytest
from solutions.y2018.solution_2018_1 import chronalCalibration, chronalCalibrationRepeat


testDataPart1 = [("+1 -2 +3 +1", 3),
                 ("+1 +1 +1", 3),
                 ("+1 +1 -2", 0),
                 ("-1 -2 -3", -6)]


@pytest.mark.parametrize("input, expected", testDataPart1)
def test_day_1_part_1(input, expected):
  assert chronalCalibration(input) == expected


testDataPart2 = [("+1 -2 +3 +1", 2),
                 ("+1 -1", 0),
                 ("+3 +3 +4 -2 -4", 10),
                 ("-6 +3 +8 +5 -6", 5),
                 ("+7 +7 -2 -7 -4", 14)]


@pytest.mark.parametrize("input, expected", testDataPart2)
def test_day_1_part_2(input, expected):
  assert chronalCalibrationRepeat(input) == expected
