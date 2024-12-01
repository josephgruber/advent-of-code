""" Advent of Code Tests - Year 2016, Day 10, Parts 1 and 2 """
from solutions.y2016.solution_2016_10 import solution


def test_2016_10_1():
  ''' Test for part 1 of solution based on provided test cases in the instructions variable. Assumes part 1 only. '''

  instructions = '''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''
  microchips = {5, 2}
  expected = 2

  assert solution(instructions, microchips, 1) == expected


def test_2016_10_2():
  ''' Test for part 2 of solution based on provided test cases in the instructions variable. Assumes part 2 only. '''

  instructions = '''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''
  microchips = {5, 2}
  expected = 30

  assert solution(instructions, microchips, 2) == expected
