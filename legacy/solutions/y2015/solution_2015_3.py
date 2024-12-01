import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from lib.helper import read_input


def sphericalHouses(directions):
  moves = {'^': (0, 1),
           'v': (0, -1),
           '>': (1, 0),
           '<': (-1, 0)}

  location = (0, 0)
  houses, roboSantaHouses = {location}, {location}

  for direction in list(directions.strip()):
    location = (location[0] + moves[direction][0], location[1] + moves[direction][1])
    houses.add(location)

  location = (0, 0)
  for direction in list(directions.strip())[::2]:
    location = (location[0] + moves[direction][0], location[1] + moves[direction][1])
    roboSantaHouses.add(location)

  location = (0, 0)
  for direction in list(directions.strip())[1::2]:
    location = (location[0] + moves[direction][0], location[1] + moves[direction][1])
    roboSantaHouses.add(location)

  return [len(houses), len(roboSantaHouses)]


def main():
  data = read_input("2015_3.txt")

  start_time = timer()
  results = sphericalHouses(data)
  end_time = timer()

  print('Part 1: ' + str(results[0]))
  print('Part 2: ' + str(results[1]))
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
