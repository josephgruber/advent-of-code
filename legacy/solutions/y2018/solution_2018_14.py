import sys  # isort:skip
import os  # isort:skip
sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from lib.helper import read_input


def chocolateChartsPart1(rounds):
  scoreboard = [3, 7]
  position = [0, 1]

  for _ in range(rounds + 10):
    newRecipes = scoreboard[position[0]] + scoreboard[position[1]]
    scoreboard.extend([int(i) for i in str(newRecipes)])
    position[0] = (position[0] + scoreboard[position[0]] + 1) % len(scoreboard)
    position[1] = (position[1] + scoreboard[position[1]] + 1) % len(scoreboard)

  return ''.join(map(str, scoreboard[rounds:rounds + 10]))


def chocolateChartsPart2(score):
  scoreboard = [3, 7]
  position = [0, 1]
  scoreLen = len(score) + 1

  while score not in ''.join(map(str, scoreboard[-scoreLen:])):
    newRecipes = scoreboard[position[0]] + scoreboard[position[1]]
    scoreboard.extend([int(i) for i in str(newRecipes)])
    position[0] = (position[0] + scoreboard[position[0]] + 1) % len(scoreboard)
    position[1] = (position[1] + scoreboard[position[1]] + 1) % len(scoreboard)

  return ''.join(map(str, scoreboard)).index(score)


def main():
  data = read_input("2018_14.txt").strip()

  start_time = timer()
  print('Part 1: ' + chocolateChartsPart1(int(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(chocolateChartsPart2(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()


if __name__ == '__main__':
  main()
