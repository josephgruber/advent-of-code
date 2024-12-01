import sys  # isort:skip
import os  # isort:skip
sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from collections import defaultdict, deque
from timeit import default_timer as timer
from lib.helper import read_input


def marbleMania(players, lastMarble):
  circle = deque([0])
  score = defaultdict(int)

  for marble in range(1, lastMarble + 1):
    player = (marble - 1) % players
    if not marble % 23:
      circle.rotate(-7)
      score[player] += marble + circle.pop()
    else:
      circle.rotate(2)
      circle.append(marble)

  return max(score.values())


def main():
  data = read_input("2018_9.txt")
  players, lastMarble = map(int, data.strip().split(', '))

  start_time = timer()
  print('Part 1: ' + str(marbleMania(players, lastMarble)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(marbleMania(players, lastMarble * 100)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()


if __name__ == '__main__':
  main()
