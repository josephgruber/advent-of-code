""" Advent of Code Tests - Year 2016, Day 10, Parts 1 and 2 """
from solutions.y2016.solution_2016_12 import solution


def test_2016_12_1():
  ''' Test for part 1 of solution based on provided test cases in the instructions variable '''

  instructions = '''cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''
  registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
  expected = 42

  assert solution(instructions, registers) == expected
