import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from lib.helper import read_input


def notQuiteLispPart1(directions):
  return sum(1 if instruction == '(' else -1 for instruction in directions.strip())


def notQuiteLispPart2(directions):
  floor = 0

  for index, instruction in enumerate(directions.strip()):
    if instruction == '(':
      floor += 1
    else:
      floor += -1

    if floor == -1:
      return index + 1


def main():
  data = read_input("2015_1.txt")

  start_time = timer()
  print('Part 1: ' + str(notQuiteLispPart1(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(notQuiteLispPart2(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()


if __name__ == '__main__':
  main()
