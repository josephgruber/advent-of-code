import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

import json
import re
from timeit import default_timer as timer
from lib.helper import read_input


def abacusFrameworkPart1(things):
  return sum(map(int, re.findall(r'[-]?\d+', things)))


def abacusFrameworkPart2(things):
  data = json.loads(s=things, object_hook=noRedObjects)

  return sum(map(int, re.findall(r'[-]?\d+', json.dumps(data))))


def noRedObjects(obj):
  if 'red' in obj.values():
    return {}

  return obj


def main():
  data = read_input("2015_12.txt")

  start_time = timer()
  print('Part 1: ' + str(abacusFrameworkPart1(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(abacusFrameworkPart2(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
