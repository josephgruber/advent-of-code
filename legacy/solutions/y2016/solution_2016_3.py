import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from lib.helper import read_input


def part1(data):
  valid = 0

  for triangle in data.splitlines():
    valid += isTriangle([int(x) for x in triangle.split()])

  return valid


def part2(data):
  valid = 0

  spec = [list(map(int, group.split())) for group in data.splitlines()]

  for row in range(0, len(spec), 3):
    for col in range(3):
      valid += isTriangle([spec[row][col], spec[row + 1][col], spec[row + 2][col]])

  return valid


def isTriangle(sides):
  sides.sort()

  if sides[0] + sides[1] > sides[2]:
    return True

  return False


def main():
  data = read_input("2016_3.txt")

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
