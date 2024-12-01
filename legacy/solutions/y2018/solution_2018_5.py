import sys  # isort:skip
import os  # isort:skip
sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

import re
import string
from timeit import default_timer as timer
from lib.helper import read_input


def alchemicalReductionPart1(polymer):
  newPolymer = None

  while (newPolymer != polymer):
    newPolymer = polymer
    polymer = re.sub(r'([a-zA-Z])(?!\1)(?i:\1)', '', polymer).strip()

  return polymer


def alchemicalReductionPart2(polymer):
  shortestPolymer = polymer

  for char in tuple(string.ascii_lowercase):
    if char not in polymer.lower():
      continue

    redactedPolymer = re.sub(r'[' + char + char.upper() + ']', '', polymer).strip()
    reactedPolymer = alchemicalReductionPart1(redactedPolymer)

    if len(reactedPolymer) < len(shortestPolymer):
      shortestPolymer = reactedPolymer

  return shortestPolymer


def main():
  data = read_input("2018_5.txt")

  start_time = timer()
  print('Part 1: ' + str(len(alchemicalReductionPart1(data))))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print("Part 2: " + str(len(alchemicalReductionPart2(data))))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
