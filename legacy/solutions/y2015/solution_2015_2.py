import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from lib.helper import read_input


def wrappingPaper(presents):
  totalWrappingPaper, totalRibbon = 0, 0

  for present in presents.splitlines():
    l, w, h = list(map(int, present.split('x')))
    surfaceArea = 2 * l * w + 2 * w * h + 2 * h * l
    smallestSide = min(l * w, w * h, h * l)
    shortestDistance = 2 * min(l + w, w + h, h + l)
    cubicFeet = l * w * h

    totalRibbon += shortestDistance + cubicFeet
    totalWrappingPaper += surfaceArea + smallestSide

  return [totalWrappingPaper, totalRibbon]


def main():
  data = read_input("2015_2.txt")

  start_time = timer()
  results = wrappingPaper(data)
  end_time = timer()

  print('Part 1: ' + str(results[0]))
  print('Part 2: ' + str(results[1]))
  print('Elapsed Time: ' + str(end_time - start_time))
  print()


if __name__ == '__main__':
  main()
