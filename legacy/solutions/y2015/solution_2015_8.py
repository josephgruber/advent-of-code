import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from lib.helper import read_input


def matchsticksPart1(strings):
  return sum((len(string) - len(eval(string)) for string in strings.splitlines()))


def matchsticksPart2(strings):
  return sum((string.count('\\') + string.count('"') + 2) for string in strings.splitlines())


def main():
  data = read_input("2015_8.txt")

  start_time = timer()
  print('Part 1: ' + str(matchsticksPart1(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(matchsticksPart2(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
