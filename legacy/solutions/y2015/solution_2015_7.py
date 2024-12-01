import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer
from collections import deque
from lib.helper import read_input


def some_assembly_required(instructions, wires=dict()):
  instructions = deque(instructions.splitlines())

  while len(instructions) > 0:
    input, output = instructions[0].strip().split(' -> ')
    input_args = input.split()
    instructions.rotate(-1)

    if output in wires:
      instructions.pop()
      continue

    if 'NOT' in input:
      if input_args[1] in wires:
        wires[output] = ~wires[input_args[1]] & 0xffff
        instructions.pop()
    elif 'AND' in input:
      if input_args[0].isdigit():
        if input_args[2] in wires:
          wires[output] = int(input_args[0]) & wires[input_args[2]]
          instructions.pop()
      else:
        if all(_ in wires for _ in (input_args[0], input_args[2])):
          wires[output] = wires[input_args[0]] & wires[input_args[2]]
          instructions.pop()
    elif 'OR' in input:
      if all(_ in wires for _ in (input_args[0], input_args[2])):
        wires[output] = wires[input_args[0]] | wires[input_args[2]]
        instructions.pop()
    elif 'LSHIFT' in input:
      if input_args[0] in wires:
        wires[output] = wires[input_args[0]] << int(input_args[2])
        instructions.pop()
    elif 'RSHIFT' in input:
      if input_args[0] in wires:
        wires[output] = wires[input_args[0]] >> int(input_args[2])
        instructions.pop()
    else:
      if input_args[0].isdigit():
        wires[output] = int(input_args[0])
        instructions.pop()
      else:
        if input_args[0] in wires:
          wires[output] = wires[input_args[0]]
          instructions.pop()

  return wires


def main():
  input = read_input("2015_7.txt")

  start_time = timer()
  results = some_assembly_required(input)
  print('Part 1: ' + str(results['a']))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  results = some_assembly_required(input, {'b': results['a']})
  print('Part 2: ' + str(results['a']))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
