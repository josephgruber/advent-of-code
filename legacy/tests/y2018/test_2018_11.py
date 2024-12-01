import pytest

from solutions.y2018.solution_2018_11 import (
    chronalChargePart1,
    chronalChargePart2,
    createGrid,
)

testDataPart1 = [(18, (33, 45), 29),
                 (42, (21, 61), 30)]

@pytest.mark.skip(reason="takes too long")
@pytest.mark.parametrize("gridSerialNumber, fuelCell, powerLevel", testDataPart1)
def test_day_11_part_1(gridSerialNumber, fuelCell, powerLevel):
  grid = createGrid(gridSerialNumber)
  assert chronalChargePart1(grid) == [fuelCell, powerLevel]


testDataPart2 = [(18, (90, 269), 16, 113),
                 (42, (232, 251), 12, 119)]

@pytest.mark.skip(reason="takes too long")
@pytest.mark.parametrize("gridSerialNumber, fuelCell, size, powerLevel", testDataPart2)
def test_day_11_part_2(gridSerialNumber, fuelCell, size, powerLevel):
  grid = createGrid(gridSerialNumber)
  assert chronalChargePart2(grid) == [fuelCell, size, powerLevel]
