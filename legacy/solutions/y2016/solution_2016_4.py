import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from collections import Counter
from re import findall
from timeit import default_timer as timer
from lib.helper import read_input


def solution(data):
  sector_sum = 0
  decrypted_rooms = []

  for room in data.splitlines():
     # Assumes a good room pattern but should check if valid room pattern
    room, sector, checksum = findall(r'([a-z-]+)(\d+)\[([a-z]+)\]', room)[0]

    if isRealRoom(room, checksum):
      sector_sum += int(sector)
      decrypted_rooms.append((sector, decrypt(room, int(sector))))

  return [sector_sum, decrypted_rooms]


def isRealRoom(room, checksum):
  room = room.replace('-', '')
  common_chars = Counter(sorted(room)).most_common(5)

  if ''.join(char for char, count in common_chars) == checksum:
    return True

  return False


def decrypt(room, sector):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  room = room.replace('-', ' ').strip()
  decrypted_value = ''

  for char in room:
    try:
      i = (alpha.index(char) + sector) % 26
      decrypted_value += alpha[i]
    except ValueError:
      decrypted_value += char

  return decrypted_value


def main():
  data = read_input("2016_4.txt")

  start_time = timer()
  answer = solution(data)
  end_time = timer()
  print('Part 1: ' + str(answer[0]))
  print('Part 2: ')
  for room in answer[1]:
    if 'north' in room[1]:
      print(room)
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
