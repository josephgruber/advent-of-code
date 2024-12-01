import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from itertools import groupby


def elvesLookElvesSay(seed, turns):  # OEIS (https://oeis.org/A005150)
  for _ in range(turns):
    seed = ''.join(str(len(list(group))) + key for key, group in groupby(seed))

  return len(seed)


def main():
  data = '1321131112'

  start_time = timer()
  print('Part 1: ' + str(elvesLookElvesSay(data, 40)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(elvesLookElvesSay(data, 50)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
