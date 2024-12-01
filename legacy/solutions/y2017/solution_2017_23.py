import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

from collections import defaultdict
from sympy import isprime # Seriously though, numpy doesn't have a primality test function?
from lib.helper import read_input


def coprocessorConflagrationPart1(instructions):
	registers = defaultdict(int)
	instructions = instructions.splitlines()
	instruction = 0
	multiplies = 0

	def value(v):
		if v.isalpha():
			return registers[v]
		else:
			return int(v)

	while instruction < len(instructions):
		op, register, val = instructions[instruction].split(" ")

		if op == "sub":
			registers[register] -= value(val)
		elif op == "mul":
			registers[register] *= value(val)
			multiplies += 1
		elif op == "set":
			registers[register] = value(val)
		elif op == "jnz":
			if value(register):
				instruction += value(val)
				continue

		instruction += 1

	return multiplies


def coprocessorConflagrationPart2():
	''' Initial values and loops calculated on Post-It notes,
	the original calculator!'''
	b = 106500
	c = 123500
	h = 0

	for valB in range(b, c + 1, 17):
		if not isprime(valB):
			h += 1

	return h


def main():
	input = read_input("2017_23.txt")
	print("Part 1: " + str(coprocessorConflagrationPart1(input)))
	print("Part 2: " + str(coprocessorConflagrationPart2()))

if __name__ == '__main__':
	main()
