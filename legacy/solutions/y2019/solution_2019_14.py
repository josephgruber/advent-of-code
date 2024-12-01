import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from lib.helper import ExecutionTimer, read_input


def part1(data):
  return None


def part2(data):
  return None


def main():
  puzzle_input = read_input('2019_.txt')

  timer = ExecutionTimer()
  print('Part 1: ' + str(part1(puzzle_input)))
  print('Elapsed Time: ' + timer.report())
  print()

  timer.start_timer()
  print('Part 2: ' + str(part2(puzzle_input)))
  print('Elapsed Time: ' + timer.report())


if __name__ == '__main__':
  main()
