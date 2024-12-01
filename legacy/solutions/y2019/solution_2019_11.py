import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from collections import defaultdict

from numpy import asarray
from PIL import Image

from lib.helper import ExecutionTimer, read_input
from lib.intcode import Intcode


def solution(intcode, start_color):
  grid = defaultdict(int)

  visited = set()

  moves = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}  # N, E, S, W
  cur_position = (0, 0)
  cur_direction = 0

  grid[cur_position] = start_color

  computer = Intcode(intcode)

  while computer.halt is False:
    try:
      computer.inputs.append(grid[cur_position])

      color = next(computer.run())
      turn = next(computer.run())

      grid[cur_position] = color
      visited.add(cur_position)

      cur_direction = (cur_direction + 1 if turn else cur_direction - 1) % 4
      cur_position = (cur_position[0] + moves[cur_direction][0], cur_position[1] + moves[cur_direction][1])
    except StopIteration:
      break

  if start_color:
    image = []
    dimensions = (max(grid, key=lambda pos: pos[0])[0], min(grid, key=lambda pos: pos[0])[0],
                  max(grid, key=lambda pos: pos[1])[1], min(grid, key=lambda pos: pos[1])[1])

    for y in range(dimensions[3], dimensions[2] + 1):
      for x in range(dimensions[1], dimensions[0] + 1):
        image.append(grid[x, y])

    image = asarray(image).reshape((dimensions[2] + 1, dimensions[0] + 1))
    Image.fromarray(image == 1).show()
  else:
    return len(visited)


def main():
  puzzle_input = read_input('2019_11.txt')

  timer = ExecutionTimer()
  print('Part 1: ' + str(solution(puzzle_input, 0)))
  print('Elapsed Time: ' + timer.report())
  print()

  timer.start_timer()
  print('Part 2')
  solution(puzzle_input, 1)
  print('Elapsed Time: ' + timer.report())


if __name__ == '__main__':
  main()
