import sys  # isort:skip
import os  # isort:skip
sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from lib.helper import read_input


def memoryManeuver(input):
  if isinstance(input, str):
    input = [int(_) for _ in input.split()]

  qtyChildNodes, qtyMetadataEntries = input[:2]
  data = input[2:]
  metadataEntries = []
  nodeValues = []

  for _ in range(qtyChildNodes):
    metadata, value, data = memoryManeuver(data)
    nodeValues.append(value)
    metadataEntries.extend(metadata)

  metadataEntries.extend(data[:qtyMetadataEntries])

  if qtyChildNodes:
    childrenNodesValue = 0
    for _ in data[:qtyMetadataEntries]:
      if _ and _ <= len(nodeValues):
        childrenNodesValue += nodeValues[_ - 1]

    return (metadataEntries, childrenNodesValue, data[qtyMetadataEntries:])

  return (metadataEntries, sum(data[:qtyMetadataEntries]), data[qtyMetadataEntries:])


def main():
  data = read_input("2018_8.txt")

  start_time = timer()
  results = memoryManeuver(data)
  end_time = timer()

  print('Part 1: ' + str(sum(results[0])))
  print('Part 2: ' + str(results[1]))
  print('Elapsed Time: ' + str(end_time - start_time))
  print()


if __name__ == '__main__':
  main()
