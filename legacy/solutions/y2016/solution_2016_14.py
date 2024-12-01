import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from collections import deque
from hashlib import md5
import re
from timeit import default_timer as timer


def solution(salt, part):
  keys = list()
  md5_hashes = deque()

  match_three = re.compile(r'(\w)\1{2}')

  i = 1000

  if part == 1:
    hashing_func = create_md5_hex
  else:
    hashing_func = create_stretched_md5_hex

  for i in range(i):
    md5_hashes.append(hashing_func(salt, str(i)))

  while len(keys) < 64:
    i += 1

    key = md5_hashes.popleft()
    md5_hashes.append(hashing_func(salt, str(i)))

    match = match_three.search(key)

    if match:
      char = match.group(1) * 5
      for hash_value in md5_hashes:
        if char in hash_value:
          keys.append(key)
          break

  return i - 1000


def create_md5_hex(salt, string):
  return md5((salt + string).encode()).hexdigest()


def create_stretched_md5_hex(salt, string):
  hash_value = create_md5_hex(salt, string)

  for _ in range(2016):
    hash_value = create_md5_hex('', hash_value)

  return hash_value


def main():
  puzzle_input = 'cuanljph'

  start_time = timer()
  print('Part 1: ' + str(solution(puzzle_input, 1)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(solution(puzzle_input, 2)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
