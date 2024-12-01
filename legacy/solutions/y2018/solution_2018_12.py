import sys  # isort:skip
import os  # isort:skip
sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from lib.helper import read_input


def subterraneanSustainability(input, generations):
  initialState, notes = input.strip().strip('initial state: ').split('\n\n')

  plants = set(i for i, c in enumerate(initialState) if c == '#')
  rules = set(note[:5] for note in notes.splitlines() if note[-1] == '#')
  for _ in range(generations):
    nextGenPlants = set()
    for i in range(min(plants) - 3, max(plants) + 4):
      if ''.join('#' if i + pot in plants else '.' for pot in [-2, -1, 0, 1, 2]) in rules:
        nextGenPlants.add(i)

    plants = nextGenPlants

  return sum(plants)


def main():
  data = read_input("2018_12.txt")

  start_time = timer()
  print('Part 1: ' + str(subterraneanSustainability(data, 20)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  # Visual inspection of the difference between generations shows after generation 108,
  # the next generation increases by 65.
  start_time = timer()
  result = subterraneanSustainability(data, 108) + (65 * (50000000000 - 108))
  print('Part 2: ' + str(result))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
