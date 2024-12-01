import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

import operator
from collections import defaultdict
from lib.helper import read_input


def duet(instructions):
	registers = defaultdict(int)
	operators = {"add": operator.add, "mul": operator.mul, "mod": operator.mod}
	instructions = instructions.splitlines()
	instruction = 0

	def value(v):
		if v.isalpha():
			return registers[v]
		else:
			return int(v)

	while True:
		if instructions[instruction].count(" ") == 2:
			op, register, val = instructions[instruction].split(" ")
		else:
			op, register = instructions[instruction].split(" ")

		if op in operators:
			registers[register] = operators[op](value(register), value(val))
		elif op == "snd":
			lastPlayed = value(register)
		elif op == "set":
			registers[register] = value(val)
		elif op == "rcv":
			if value(register):
				return(lastPlayed)
		elif op == "jgz":
			if value(register):
				instruction += value(val)
				continue

		instruction += 1


def main():
	input = read_input("2017_18.txt")
	print("Part 1: " + str(duet(input)))


if __name__ == '__main__':
	main()
