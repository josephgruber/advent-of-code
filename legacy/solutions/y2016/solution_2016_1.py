import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from lib.helper import read_input


def solution(input):
  position = [0, 0]
  orientation = 0
  visits = []
  revisit = None

  for move in input.split(', '):
    direction = move[0]
    distance = int(move[1:])

    if direction == 'R':  # 0 = N, 1 = E, 2 = S, 3 = W
      orientation = (orientation + 1) % 4
    else:
      orientation = (orientation - 1) % 4

    for _ in range(distance):
      if orientation < 2:
        position[orientation % 2] += 1
      else:
        position[orientation % 2] -= 1

      if position in visits and revisit is None:
        revisit = abs(position[0]) + abs(position[1])

      visits.append(position[:])

  return [abs(position[0]) + abs(position[1]), revisit]


def main():
  data = read_input("2016_1.txt")

  start_time = timer()
  results = solution(data)
  print('Part 1: ' + str(results[0]))
  print('Part 2: ' + str(results[1]))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
