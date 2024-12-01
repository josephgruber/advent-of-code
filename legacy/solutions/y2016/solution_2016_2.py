import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from lib.helper import read_input


def part1(input):
  code = ''
  dialpad = {(-1, 1): '1', (0, 1): '2', (1, 1): '3', (-1, 0): '4', (0, 0): '5', (1, 0): '6', (-1, -1): '7',
             (0, -1): '8', (1, -1): '9'}
  movement = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
  position = (0, 0)

  for instructions in input.splitlines():
    for instruction in instructions:
      new_position = tuple(current_position + move for current_position, move in zip(position, movement[instruction]))

      if new_position[0] < -1 or new_position[0] > 1 or new_position[1] < -1 or new_position[1] > 1:
        continue

      position = new_position

    code = code + dialpad[position]

  return int(code)


def part2(input):
  code = ''
  dialpad = {(0, 2): '1', (-1, 1): '2', (0, 1): '3', (1, 1): '4', (-2, 0): '5', (-1, 0): '6', (0, 0): '7',
             (1, 0): '8', (2, 0): '9', (-1, -1): 'A', (0, -1): 'B', (1, -1): 'C', (0, -2): 'D'}
  movement = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
  position = (-2, 0)

  for instructions in input.splitlines():
    for instruction in instructions:
      new_position = tuple(current_position + move for current_position, move in zip(position, movement[instruction]))

      if new_position in dialpad:
        position = new_position
      else:
        continue

    code = code + dialpad[position]

  return code


def main():
  data = read_input("2016_2.txt")

  start_time = timer()
  print('Part 1: ' + str(part1(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(part2(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
