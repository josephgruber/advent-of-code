""" Advent of Code Solution - Year 2016, Day 10, Parts 1 and 2 """
import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from timeit import default_timer as timer

from lib.helper import read_input


def solution(data, microchips, part):
  """ Loops through the set of instructions provided creating three dictionaries, one for bots, another for outputs, and
  another for the remaining instructions. Initially populates the bots dictionary with initial bot assignments then
  runs through the remaining instructions. For part 1, breaks once the values being searched for are found. For part 2,
  runs to completion and then returns the value of outputs 0, 1, and 2 multiplied together.

  Arguments:
      data {str} -- Multi-line string with instructions for bots to perform
      microchips {set} -- Set of two integers which are being looked for
      part {int} -- Determines whether part 1 or part 2 of the problem is being solved

  Returns:
      [int] -- Returns the index of bots which has the value of microchips for part 1,
              otherwise returns the value of outputs 0, 1, and 2 for part 2
  """

  bots = dict()
  outputs = dict()
  instructions = dict()

  for instruction in data.splitlines():
    if instruction[:5] == 'value':
      value, bot = map(int, instruction[6:].split(' goes to bot '))

      if bot in bots:
        bots[bot].add(value)
      else:
        bots[bot] = {value}
    else:
      bot, low_dest, low_id, high_dest, high_id = (
          instruction[4:].replace(' gives low to', '').replace('and high to ', '').split()
      )
      instructions[int(bot)] = {'low': [low_dest, int(low_id)], 'high': [high_dest, int(high_id)]}

  while True:
    if part == 1 and microchips in bots.values():
      return list(bots.keys())[list(bots.values()).index(microchips)]
    elif part == 2 and 0 in outputs and 1 in outputs and 2 in outputs:
      return list(outputs[0])[0] * list(outputs[1])[0] * list(outputs[2])[0]

    for bot in bots:
      if len(bots[bot]) == 2:
        min_value = min(bots[bot])
        max_value = max(bots[bot])

        if instructions[bot]['low'][0] == 'output':
          if instructions[bot]['low'][1] in outputs:
            outputs[instructions[bot]['low'][1]].add(min_value)
          else:
            outputs[instructions[bot]['low'][1]] = {min_value}
        else:
          if instructions[bot]['low'][1] in bots:
            bots[instructions[bot]['low'][1]].add(min_value)
          else:
            bots[instructions[bot]['low'][1]] = {min_value}

        if instructions[bot]['high'][0] == 'output':
          if instructions[bot]['high'][1] in outputs:
            outputs[instructions[bot]['high'][1]].add(max_value)
          else:
            outputs[instructions[bot]['high'][1]] = {max_value}
        else:
          if instructions[bot]['high'][1] in bots:
            bots[instructions[bot]['high'][1]].add(max_value)
          else:
            bots[instructions[bot]['high'][1]] = {max_value}

        bots[bot] = {}
        break


def main():
  ''' Main function to run both part 1 and part 2 solutions including timing '''
  data = read_input("2016_10.txt")

  start_time = timer()
  print('Part 1: ' + str(solution(data, {61, 17}, 1)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))
  print()

  start_time = timer()
  print('Part 2: ' + str(solution(data, {61, 17}, 2)))
  end_time = timer()
  print('Elapsed Time: ' + str(end_time - start_time))


if __name__ == '__main__':
  main()
