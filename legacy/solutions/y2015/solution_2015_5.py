import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

import re
from timeit import default_timer as timer
from lib.helper import read_input


def intern_elves(data):
  return [sum(part1(string.strip()) for string in data.splitlines()),
          sum(part2(string.strip()) for string in data.splitlines())]


def part1(line):
  return bool(re.search(r'([aeiou].*){3,}', line) and re.search(r'([a-z])\1',
                                                                line) and not re.search(r'(ab|cd|pq|xy)', line))


def part2(line):
  return bool(re.search(r'([a-z]{2}).*\1', line) and re.search(r'([a-z]).\1', line))


def main():
  data = read_input("2015_5.txt")

  start_time = timer()
  results = intern_elves(data)
  end_time = timer()

  print('Part 1: ' + str(results[0]))
  print('Part 2: ' + str(results[1]))
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
