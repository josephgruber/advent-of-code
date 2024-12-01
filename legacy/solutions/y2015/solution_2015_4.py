import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

import hashlib
from timeit import default_timer as timer
from lib.helper import read_input


def stockingStuffer(key, search):
  i = 1
  key = key.strip()
  index = len(search)

  while True:
    if hashlib.md5((key + str(i)).encode()).hexdigest()[:index] == search:
      return i

    i += 1


def main():
  data = read_input("2015_4.txt")

  start_time = timer()
  print('Part 1: ' + str(stockingStuffer(data, '00000')))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(stockingStuffer(data, '000000')))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
