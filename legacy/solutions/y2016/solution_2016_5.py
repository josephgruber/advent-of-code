import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from hashlib import md5
from timeit import default_timer as timer
from lib.helper import read_input


def solution(input, position=None):
  i = 0
  password = {}
  pos = 0
  possible_positions = range(8)

  while len(password) != 8:
    digest = md5((input + str(i)).encode()).hexdigest()

    if digest.startswith('00000'):
      if position is None:
        password[pos] = digest[5]
        pos += 1
      else:
        pos = int(digest[5], 16)
        if pos in possible_positions and pos not in password:
          password[pos] = digest[6]

    i += 1

  return ''.join(password[x] for x in sorted(password))


def main():
  input = read_input("2016_5.txt")

  start_time = timer()
  print('Part 1: ' + str(solution(input.strip())))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(solution(input.strip(), position=True)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
