''' Advent of Code Solution - Year 2016, Day 9, Parts 1 and 2 '''
import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from lib.helper import read_input


def part1(compressed_str):
  uncompressed_str = ''

  while '(' in compressed_str:
    marker_s = compressed_str.find('(')
    marker_e = compressed_str.find(')', marker_s)
    chars, repeat = map(int, compressed_str[marker_s + 1:marker_e].split('x'))

    uncompressed_str += compressed_str[:marker_s]
    uncompressed_str += (compressed_str[marker_e + 1:marker_e + 1 + chars] * repeat)
    compressed_str = compressed_str[marker_e + 1 + chars:]

  uncompressed_str += compressed_str

  return len(uncompressed_str.strip())


def part2(compressed_str):
  uncompressed = [1] * len(compressed_str.strip())
  uncompressed_length = 0

  idx = 0

  while idx < len(compressed_str.strip()):
    if compressed_str[idx] == '(':
      marker_e = compressed_str.find(')', idx)
      chars, repeat = map(int, compressed_str[idx + 1:marker_e].split('x'))

      uncompressed[marker_e + 1:marker_e + 1 + chars] = [val * repeat
                                                         for val in uncompressed[marker_e + 1:marker_e + 1 + chars]]

      idx = marker_e + 1
    else:
      uncompressed_length += uncompressed[idx]
      idx += 1

  return uncompressed_length


def main():
  data = read_input("2016_9.txt")

  start_time = timer()
  print('Part 1: ' + str(part1(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(part2(data)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
