""" Advent of Code Solution - Year 2016, Day 12, Parts 1 and 2 """
import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from lib.helper import read_input


def solution(instructions, registers):
  """Loops through the input line by line, and performs the specified instruction (cpy, inc, dec, jnz)
  on the value stored in the register

  Arguments:
      instructions {[type]} -- multi-line input of logic to perform based on the pre-defined rules
      registers {dict} -- dictionary of pre-determined registers for each part of the puzzle that
      the instructions are then performed on

  Returns:
      int -- value of 'a' from the registers after looping through all steps in instructions
  """

  def get_value(idx):
    return registers[idx] if idx in registers else int(idx)

  instructions = instructions.splitlines()

  index = 0

  while index < len(instructions):
    instruction, x, *y = instructions[index].split()

    if instruction == 'cpy':
      registers[y[0]] = get_value(x)
    elif instruction == 'inc':
      registers[x] += 1
    elif instruction == 'dec':
      registers[x] -= 1
    elif instruction == 'jnz':
      if get_value(x):
        index += int(y[0])
        continue

    index += 1

  return registers['a']


def main():
  ''' Main function to run both part 1 and part 2 solutions including timing '''
  data = read_input("2016_12.txt")

  start_time = timer()
  print('Part 1: ' + str(solution(data, {'a': 0, 'b': 0, 'c': 0, 'd': 0})))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(solution(data, {'a': 0, 'b': 0, 'c': 1, 'd': 0})))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
