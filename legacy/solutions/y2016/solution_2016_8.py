import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
import numpy as np
from lib.helper import read_input


def solution(input):
  grid = np.full([6, 50], False, dtype=bool)

  for instruction in input.splitlines():
    components = instruction.split()

    if components[0] == 'rect':
      width, height = map(int, components[1].split('x'))
      grid[:height, :width] = True
    elif components[0] == 'rotate':
      rot = int(components[2].split('=')[1])
      shift = int(components[4])

      if components[1] == 'row':
        grid[rot] = np.roll(grid[rot], shift)
      elif components[1] == 'column':
        grid.T[rot] = np.roll(grid.T[rot], shift)

  for row in grid:
    for col in row:
      print('#', end='') if col else print('-', end='')
    print('\n', end='')

  return np.count_nonzero(grid)


def main():
  input = read_input("2016_8.txt")

  start_time = timer()
  print('Part 1: ' + str(solution(input)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
