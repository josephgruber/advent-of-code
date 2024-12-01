from lib.helper import read_input, cube_distance
import sys
import os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")


def hexEdPart1(data):
  neighbors = {"ne": (1, 0, -1),
               "n": (0, 1, -1),
               "nw": (-1, 1, 0),
               "sw": (-1, 0, 1),
               "s": (0, -1, 1),
               "se": (1, -1, 0)}
  position = [0, 0, 0]

  for move in data.split(","):
    position[0] += neighbors[move.strip()][0]
    position[1] += neighbors[move.strip()][1]
    position[2] += neighbors[move.strip()][2]

  steps = cube_distance(position[0], position[1], position[2])

  return steps


def hexEdPart2(data):
  neighbors = {"ne": (1, 0, -1),
               "n": (0, 1, -1),
               "nw": (-1, 1, 0),
               "sw": (-1, 0, 1),
               "s": (0, -1, 1),
               "se": (1, -1, 0)}
  position = [0, 0, 0]
  distance = []

  for move in data.split(","):
    position[0] += neighbors[move.strip()][0]
    position[1] += neighbors[move.strip()][1]
    position[2] += neighbors[move.strip()][2]
    distance.append(cube_distance(position[0], position[1], position[2]))

  return max(distance)


def main():
  input = read_input("2017_11.txt")
  print("Part 1: " + str(hexEdPart1(input)))
  print("Part 2: " + str(hexEdPart2(input)))


if __name__ == '__main__':
  main()
