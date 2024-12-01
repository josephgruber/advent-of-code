import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from string import ascii_lowercase
import re


def corporatePolicy(password):
  chars = [c for c in ascii_lowercase if c not in ['i', 'o', 'l']]
  chars.append('#')

  def newPassword():
    if password[-1] == '#':
      rootPassword = password[:password.index('#')]
      return rootPassword[:-1] + \
          chars[chars.index(rootPassword[-1]) + 1] + \
          ('a' * (len(password) - len(rootPassword)))

    return password[:-1] + chars[chars.index(password[-1]) + 1]

  password = newPassword()

  while not isValidPassword(password):
    password = newPassword()
    while '#' in password:
      password = newPassword()

  return password


def isValidPassword(password):
  if not any([ascii_lowercase[_:_ + 3] in password for _ in range(24)]):  # rule 1
    return False

  if re.search(r'.*[iol]+.*', password):  # rule 2
    return False

  if len(re.findall(r'([a-z])\1', password)) < 2:  # rule 3
    return False

  return True


def main():
  data = 'vzbxkghb'

  start_time = timer()
  result = corporatePolicy(data)
  print('Part 1: ' + result)
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + corporatePolicy(result))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
