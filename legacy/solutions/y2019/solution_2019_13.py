import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from lib.helper import ExecutionTimer, read_input
from lib.intcode import Intcode


def part1(intcode):
  grid = dict()

  computer = Intcode(intcode)
  output = list(computer.run())

  for instruction in chunk(output, 3):
    x, y, tile_id = instruction

    if (x, y) in grid.keys():
      if grid[(x, y)] == 2 and tile_id == 4:
        grid[(x, y)] = tile_id
    else:
      grid[(x, y)] = tile_id

  return len([val for val in grid.values() if val == 2])


def part2(intcode):
  grid = dict()

  current_score = 0
  ball_loc = 0
  paddle_loc = 0

  computer = Intcode(intcode)
  computer.program[0] = 2  # Insert two quarters

  while computer.halt is False:
    try:
      x = next(computer.run())
      y = next(computer.run())
      tile_id = next(computer.run())

      if x == -1 and y == 0:
        current_score = tile_id
        continue

      if tile_id in (3, 4):
        if tile_id == 3:
          paddle_loc = x

        if tile_id == 4:
          ball_loc = x

        computer.inputs = [-1 if ball_loc < paddle_loc else 1 if ball_loc > paddle_loc else 0]

      if (x, y) in grid.keys():
        if grid[(x, y)] == 2 and tile_id == 4:
          grid[(x, y)] = tile_id
      else:
        grid[(x, y)] = tile_id
    except StopIteration:
      break

  return current_score


def chunk(instruction_list, size):
  for i in range(0, len(instruction_list), size):
    yield instruction_list[i:i + size]


def main():
  puzzle_input = read_input('2019_13.txt')

  timer = ExecutionTimer()
  print('Part 1: ' + str(part1(puzzle_input)))
  print('Elapsed Time: ' + timer.report())
  print()

  timer.start_timer()
  print('Part 2: ' + str(part2(puzzle_input)))
  print('Elapsed Time: ' + timer.report())


if __name__ == '__main__':
  main()
