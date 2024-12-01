import sys  # isort:skip
import os  # isort:skip
sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from collections import Counter
from itertools import combinations
from timeit import default_timer as timer
from lib.helper import read_input


def invMgmtSystemPart1(boxes):
  boxCountA = 0
  boxCountB = 0

  for box in boxes.splitlines():
    boxId = Counter(box.strip())
    checksumBoxes = {x: boxId[x] for x in boxId if boxId[x] == 2 or boxId[x] == 3}

    if 2 in checksumBoxes.values():
      boxCountA += 1

    if 3 in checksumBoxes.values():
      boxCountB += 1

  return boxCountA * boxCountB


def invMgmtSystemPart2(boxes):
  for boxA, boxB in combinations(boxes.splitlines(), 2):
    boxDiff = [a for a, b in zip(boxA, boxB) if a == b]
    if len(boxA) - len(boxDiff) == 1:
      return ''.join(boxDiff)


def main():
  input = read_input("2018_2.txt")

  start_time = timer()
  print("Part 1: " + str(invMgmtSystemPart1(input)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print("Part 2: " + str(invMgmtSystemPart2(input)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
