import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from collections import Counter
from lib.helper import read_input


def solution(input):
  most_common = ''
  least_common = ''

  for bit in zip(*input.splitlines()):
    error_corrected = Counter(''.join(bit)).most_common()
    most_common += error_corrected[0][0]
    least_common += error_corrected[-1][0]

  return [most_common, least_common]


def main():
  input = read_input("2016_6.txt")

  start_time = timer()
  answer = solution(input)
  end_time = timer()

  print('Part 1: ' + str(answer[0]))
  print('Part 2: ' + str(answer[1]))
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
