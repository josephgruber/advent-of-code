import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from typing import Dict, List, Tuple

from lib.helper import ExecutionTimer, read_input
from lib.intcode import Intcode


def part1(intcode: str) -> int:
  grid: Dict[Tuple[int, int], str] = create_grid(intcode)

  intersections: List[Tuple[int, int]] = get_alignment_parameters(grid)

  alignment_parameters: int = sum([intersection[0] * intersection[1] for intersection in intersections])

  return alignment_parameters


def part2(intcode: str) -> int:
  prompt: str = ''
  status: int = 0
  computer: Intcode = Intcode(intcode)

  computer.program[0] = 2

  while computer.halt is False:
    try:
      status = next(computer.run())

      if status in (35, 46, 94):
        prompt = ''
        continue

      prompt += chr(status)

      if prompt == '\n':
        prompt = ''
        continue

      if prompt == 'Main:\n':
        computer.inputs = [ord(c) for c in 'A,B,A,B,A,C,B,C,A,C\n']
        prompt = ''

      if prompt == 'Function A:\n':
        computer.inputs = [ord(c) for c in 'R,4,L,10,L,10\n']
        prompt = ''

      if prompt == 'Function B:\n':
        computer.inputs = [ord(c) for c in 'L,8,R,12,R,10,R,4\n']
        prompt = ''

      if prompt == 'Function C:\n':
        computer.inputs = [ord(c) for c in 'L,8,L,8,R,10,R,4\n']
        prompt = ''

      if prompt == 'Continuous video feed?\n':
        computer.inputs = [ord(c) for c in 'n\n']
        prompt = ''
    except StopIteration:
      break

  return status


def create_grid(intcode: str) -> Dict[Tuple[int, int], str]:
  grid: Dict[Tuple[int, int], str] = dict()
  current_pos: Tuple[int, int] = (0, 0)

  computer: Intcode = Intcode(intcode)

  while computer.halt is False:
    try:
      camera_output: int = next(computer.run())

      if camera_output == 10:
        current_pos = (current_pos[0] + 1, 0)
      else:
        grid[current_pos] = chr(camera_output)
        current_pos = (current_pos[0], current_pos[1] + 1)
    except StopIteration:
      break

  return grid


def get_alignment_parameters(grid: Dict[Tuple[int, int], str]) -> List[Tuple[int, int]]:
  intersections: List[Tuple[int, int]] = []

  for key, val in grid.items():
    if val == '#':
      neighbors: List[Tuple[int, int]] = [(key[0], key[1] + 1), (key[0], key[1] - 1),
                                          (key[0] + 1, key[1]), (key[0] - 1, key[1])]

      if neighbors[0] in grid and neighbors[1] in grid and neighbors[2] in grid and neighbors[3] in grid:
        if grid[neighbors[0]] == '#' and grid[neighbors[1]] == '#' and \
                grid[neighbors[2]] == '#' and grid[neighbors[3]] == '#':
          intersections.append(key)
          grid[key] = 'O'

  return intersections


def main():
  puzzle_input = read_input('2019_17.txt')

  timer = ExecutionTimer()
  result: int = part1(puzzle_input)
  print(f'Part 1: {result}')
  print('Elapsed Time: ' + timer.report())
  print()

  timer.start_timer()
  print('Part 2: ' + str(part2(puzzle_input)))
  print('Elapsed Time: ' + timer.report())


if __name__ == '__main__':
  main()
