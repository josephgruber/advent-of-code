import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from lib.helper import read_file_by_line, rootdir


def validatePassphrasePart1(passphrase):
  words = passphrase.split()

  if len(words) != len(set(words)):
    return False
  else:
    return True


def validatePassphrasePart2(passphrase):
  words = passphrase.split()
  alphaWords = [''.join(sorted(word)) for word in words]

  if len(alphaWords) != len(set(alphaWords)):
    return False
  else:
    return True


def checkPassphraseListPart1(location):
  totalValid = 0

  for line in read_file_by_line(location):
    if(validatePassphrasePart1(line.strip())):
      totalValid += 1

  return totalValid


def checkPassphraseListPart2(location):
  totalValid = 0

  for line in read_file_by_line(location):
    if(validatePassphrasePart2(line.strip())):
      totalValid += 1

  return totalValid


def main():
  input = rootdir() + "/inputs/2017_4.txt"
  print("Part 1: " + str(checkPassphraseListPart1(input)))
  print("Part 2: " + str(checkPassphraseListPart2(input)))


if __name__ == '__main__':
  main()
