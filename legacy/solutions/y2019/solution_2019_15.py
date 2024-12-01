import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from collections import deque
from typing import Deque, Dict, List, Set, Tuple

from lib.helper import ExecutionTimer, read_input
from lib.intcode import Intcode


def solution(intcode: str) -> List[int]:
  grid = create_grid(intcode)

  shortest_path_to_o2: int = grid[(99, 99)]
  del grid[(99, 99)]

  time_to_full_o2: int = enable_o2(grid)

  return [shortest_path_to_o2, time_to_full_o2]


def create_grid(intcode: str) -> Dict[Tuple[int, int], int]:
  directions: Tuple[int, int, int, int] = (1, 2, 3, 4)  # North: 1, South: 2, West: 3, East: 4
  reverse_directions: List[int] = [0, 2, 1, 4, 3]
  moves: Dict[int, Tuple[int, int]] = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}  # North, South, West, East
  current_position: Tuple[int, int] = (0, 0)
  visited: Dict[Tuple[int, int], Set[int]] = dict()
  grid: Dict[Tuple[int, int], int] = dict({current_position: 1})

  next_move: List[int] = [1]  # Move north first
  next_position: Tuple[int, int] = (0, 0)  # Start at x = 0, y = 0
  backtrack: bool = False
  path: Deque[int] = deque([])

  computer: Intcode = Intcode(intcode)

  while computer.halt is False:
    try:
      if backtrack:
        next_move = [reverse_directions[path.pop()]]

      next_position = (current_position[0] + moves[next_move[0]][0],
                       current_position[1] + moves[next_move[0]][1])

      computer.inputs.append(next_move[0])

      status: int = next(computer.run())
      grid[next_position] = status

      if current_position in visited:
        visited[current_position].add(next_move[0])
      else:
        visited[current_position] = {next_move[0]}

      if next_position in visited:
        visited[next_position].add(reverse_directions[next_move[0]])
      else:
        visited[next_position] = {reverse_directions[next_move[0]]}

      if status != 0:
        current_position = next_position

        if not backtrack:
          path.append(next_move[0])

        if status == 2:
          grid[(99, 99)] = len(path) if (99, 99) not in grid else min(grid[(99, 99)], len(path))

      next_move = list(set(directions) - visited[current_position])

      backtrack = not bool(next_move)

      if current_position == (0, 0) and len(visited[(0, 0)]) == 4:
        break  # Back to start and all locations have been visited
    except StopIteration:
      break

  return grid


def enable_o2(grid: Dict[Tuple[int, int], int]) -> int:
  positions: List[Tuple] = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]
  steps: int = 0

  while 1 in grid.values():
    for key, val in grid.items():
      if val == 2:
        for position in positions:
          neighbor: Tuple[int, int] = (key[0] + position[0], key[1] + position[1])
          if neighbor in grid and grid[neighbor] == 1:
            grid[neighbor] = 3

    for key, val in grid.items():
      if val == 3:
        grid[key] = 2

    steps += 1

  return steps


def main():
  puzzle_input: str = read_input('2019_15.txt')

  timer: ExecutionTimer = ExecutionTimer()
  result: List[int] = solution(puzzle_input)
  print('Part 1: ' + str(result[0]))
  print('Part 2: ' + str(result[1]))
  print('Elapsed Time: ' + timer.report())


if __name__ == '__main__':
  main()
