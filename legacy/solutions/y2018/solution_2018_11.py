import sys  # isort:skip
import os  # isort:skip
sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
import numpy as np
from lib.helper import read_input


def createGrid(serialNumber):
  grid = np.zeros((301, 301))

  for y in range(1, 301):
    for rackId in range(11, 311):
      powerLevel = ((rackId * y) + serialNumber) * rackId
      grid[rackId - 10][y] = (powerLevel // 100 % 10) - 5

  return grid


def chronalChargePart1(grid):
  maxPowerLevel = 0
  fuelCell = (0, 0)

  for x in range(298):
    for y in range(298):
      powerLevel = np.sum(grid[x:x + 3, y:y + 3])

      if powerLevel > maxPowerLevel:
        maxPowerLevel = powerLevel
        fuelCell = (x, y)

  return [fuelCell, maxPowerLevel]


def chronalChargePart2(grid):
  maxPowerLevel = 0
  fuelCell = (0, 0)
  fuelCellSize = 0

  for size in range(1, 301):
    for x in range(301 - size):
      for y in range(301 - size):
        powerLevel = np.sum(grid[x:x + size, y:y + size])

        if powerLevel > maxPowerLevel:
          maxPowerLevel = powerLevel
          fuelCell = (x, y)
          fuelCellSize = size

  return [fuelCell, fuelCellSize, maxPowerLevel]


def main():
  data = read_input("2018_11.txt")

  start_time = timer()
  grid = createGrid(int(data))
  end_time = timer()
  print('Elapsed Time (Grid Creation): ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 1: ' + str(chronalChargePart1(grid)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(chronalChargePart2(grid)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()


if __name__ == '__main__':
  main()
