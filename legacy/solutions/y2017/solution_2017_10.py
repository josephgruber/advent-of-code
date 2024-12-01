from lib.helper import knot_hash
import sys
import os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")


def knotHashPart1(lengths, listSize):
  skipSize, position = 0, 0
  l = list(range(listSize))

  for length in lengths:
    if length <= 1:
      position = position + length + skipSize
      skipSize += 1
      continue

    if length > len(l) - position:
      sublist = list(l[position:] + l[0:length - (len(l) - position)])[::-1]
      l[position:] = sublist[0:len(l) - position]
      del sublist[0:len(l) - position]
      l[0:len(sublist)] = sublist
    else:
      l[position:length + position] = l[position:length + position][::-1]

    position = position + length + skipSize
    if position > listSize:
      while position > listSize:
        position = position - listSize

    skipSize += 1

  return l[0] * l[1]


def main():
  input = 83, 0, 193, 1, 254, 237, 187, 40, 88, 27, 2, 255, 149, 29, 42, 100
  size = 256
  print("Part 1: " + str(knotHashPart1(input, size)))

  input = "83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100"
  print("Part 2: " + knot_hash(input))


if __name__ == '__main__':
  main()
