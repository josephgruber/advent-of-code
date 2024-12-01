import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from lib.helper import read_input


def reindeerOlympics(reindeerMeta, time):
  distances = dict()

  for reindeer in reindeerMeta.splitlines():
    reindeer = reindeer.split()
    name, speed, flyingTime, restTime = [reindeer[0], int(reindeer[3]), int(reindeer[6]), int(reindeer[13])]

    if time // (flyingTime + restTime) < time:
      distance = (time // (flyingTime + restTime)) * (flyingTime * speed)
      remainingTime = time - ((time // (flyingTime + restTime)) * (flyingTime + restTime))

      if flyingTime > remainingTime:
        distances[name] = distance + (remainingTime * speed)
      else:
        distances[name] = distance + (flyingTime * speed)
    else:
      distances[name] = (time // (flyingTime + restTime)) * (flyingTime * speed)

  return max(distances.values())


def main():
  data = read_input("2015_14.txt")

  start_time = timer()
  print('Part 1: ' + str(reindeerOlympics(data, 2503)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()


if __name__ == '__main__':
  main()
