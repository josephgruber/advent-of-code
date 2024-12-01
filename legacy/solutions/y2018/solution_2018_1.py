import sys  # isort:skip
import os  # isort:skip
sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from itertools import cycle
from timeit import default_timer as timer
from lib.helper import read_input


def chronalCalibration(input):
  return sum(int(change) for change in input.split())


def chronalCalibrationRepeat(input):
  frequency = 0
  frequencyValues = {frequency}

  for change in cycle(input.split()):
    frequency += int(change)

    if frequency in frequencyValues:
      break

    frequencyValues.add(frequency)

  return frequency


def main():
  data = read_input("2018_1.txt")

  start_time = timer()
  print("Part 1: " + str(chronalCalibration(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print("Part 2: " + str(chronalCalibrationRepeat(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
