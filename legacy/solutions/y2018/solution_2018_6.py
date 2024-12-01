import sys  # isort:skip
import os  # isort:skip
sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from collections import Counter
from timeit import default_timer as timer
from lib.helper import manhattan_distance, read_input


def chronalCoordinates(input, totalDistance=None):
  areaCount = Counter()

  coordinates = [tuple(int(_) for _ in line.strip().split(', ')) for line in input.splitlines()]

  minX = min([x for x, y in coordinates])
  maxX = max([x for x, y in coordinates])
  minY = min([y for x, y in coordinates])
  maxY = max([y for x, y in coordinates])

  for i in range(minX, maxX):
    for x in range(minY, maxY):
      distance = [manhattan_distance((i, x), position) for position in coordinates]
      sortedDistance = sorted(distance)

      if sortedDistance[0] != sortedDistance[1]:
        minimumDistance = distance.index(min(distance))
        areaCount[coordinates[minimumDistance]] += 1

  largestDistance = 0
  for position in coordinates:
    if minX < position[0] < maxX and minY < position[1] < maxY:
      largestDistance = max(largestDistance, areaCount[position])

  region = 0
  if totalDistance is not None:
    for i in range(minX, maxX):
      for x in range(minY, maxY):
        distance = [manhattan_distance((i, x), c) for c in coordinates]
        if sum(distance) < totalDistance:
          region += 1

  return [largestDistance, region]


def main():
  data = read_input("2018_6.txt")

  start_time = timer()
  result = chronalCoordinates(data, 10000)
  end_time = timer()

  print('Part 1: ' + str(result[0]))
  print('Part 2: ' + str(result[1]))
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
