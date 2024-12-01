import sys  # isort:skip
import os  # isort:skip
sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
import numpy as np
from lib.helper import read_input

fabric = np.zeros((1000, 1000))


def fabricClaimsPart1(claims):
  for claim in claims.splitlines():
    _id, x, y, dx, dy = parseClaim(claim)
    fabric[x: x + dx, y: y + dy] += 1

  overlap = np.sum(fabric > 1)

  return overlap


def fabricClaimsPart2(claims):
  if np.all(fabric[0: 1000, 0: 1000] == 0):
    fabricClaimsPart1(claims)

  for claim in claims.splitlines():
    id, x, y, dx, dy = parseClaim(claim)

    if np.all(fabric[x: x + dx, y: y + dy] == 1):
      return id


def parseClaim(claim):
  claimComponents = claim.strip().split()

  claimId = int(claimComponents[0][1:].strip())
  claimX, claimY = map(int, claimComponents[2][:-1].strip().split(','))
  claimWidth, claimHeight = map(int, claimComponents[3].strip().split('x'))

  return claimId, claimX, claimY, claimWidth, claimHeight


def main():
  data = read_input("2018_3.txt")

  start_time = timer()
  print("Part 1: " + str(fabricClaimsPart1(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print("Part 2: " + str(fabricClaimsPart2(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
