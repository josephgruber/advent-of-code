import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from re import search, split
from timeit import default_timer as timer
from regex import finditer
from lib.helper import read_input


def part1(input):
  tls = 0

  for ip_address in input.splitlines():
    inside_abba = False
    outside_abba = False

    components = split(r'\[|\]', ip_address)
    supernet_seq = components[::2]
    hypernet_seq = components[1::2]

    for seq in supernet_seq:
      if isAbba(seq):
        outside_abba = True
        break

    if outside_abba:
      for seq in hypernet_seq:
        if isAbba(seq):
          inside_abba = True
          break

    if outside_abba and not inside_abba:
      tls += 1

  return tls


def part2(input):
  ssl = 0

  for ip_address in input.splitlines():
    components = split(r'\[|\]', ip_address)
    supernet_seq = components[::2]
    hypernet_seq = components[1::2]

    for seq in supernet_seq:
      for match in finditer(r'([\w])((?!\1)[\w])\1', seq, overlapped=True):
        if isBab(match, hypernet_seq):
          ssl += 1
          break

  return ssl


def isAbba(octet):
  return bool(search(r'([\w])((?!\1)[\w])\2\1', octet))


def isBab(aba, hypernet):
  for seq in hypernet:
    if ''.join(aba[0][1] + aba[0][0] + aba[0][1]) in seq:
      return True

  return False


def main():
  data = read_input("2016_7.txt")

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
