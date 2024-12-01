import sys  # isort:skip
import os  # isort:skip
sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

import re
from timeit import default_timer as timer
import numpy as np
from lib.helper import read_input


def starAlignment(input):
  minPosition = None
  time = 0
  points = [[int(_) for _ in re.findall(r'-?\d+', point)] for point in input.splitlines()]

  while True:
    minX = min(x + time * vx for (x, y, vx, vy) in points)
    maxX = max(x + time * vx for (x, y, vx, vy) in points)
    minY = min(y + time * vy for (x, y, vx, vy) in points)
    maxY = max(y + time * vy for (x, y, vx, vy) in points)
    newPosition = maxX - minX + maxY - minY

    if minPosition is None or minPosition > newPosition:
      minPosition = newPosition
      time += 1
    else:
      return time - 1


def printResult(input, time):
  points = [[int(_) for _ in re.findall(r'-?\d+', point)] for point in input.splitlines()]

  maxX = max(x + time * vx for (x, y, vx, vy) in points)
  maxY = max(y + time * vy for (x, y, vx, vy) in points)
  maxGrid = max(maxX, maxY) + 1
  grid = np.full((maxGrid, maxGrid), ' ')

  for (x, y, vx, vy) in points:
    grid[y + time * vy][x + time * vx] = '#'

  for _ in grid:
    if ''.join(_).strip():
      print(''.join(_).strip())


def main():
  data = read_input("2018_10.txt")

  start_time = timer()
  result = starAlignment(data)
  print('Part 1: ')
  printResult(data, result)
  print('Part 2: ' + str(result))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
