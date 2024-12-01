import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

import operator
from lib.helper import read_input
from collections import defaultdict


def processInstructionsPart1(data):
	registers = defaultdict(int)

	operators = {
		"<": operator.lt,
		">": operator.gt,
		"==": operator.eq,
		"!=": operator.ne,
		">=": operator.ge,
		"<=": operator.le,
		"inc": operator.add,
		"dec": operator.sub
	}

	for instructions in data.splitlines():
		register, operation, value, _, conditionRegister, conditionOperation, conditionValue = instructions.split()

		if operators[conditionOperation](registers[conditionRegister], int(conditionValue)):
			registers[register] = operators[operation](registers[register], int(value))

	return max(registers.values())


def processInstructionsPart2(data):
	registers = defaultdict(int)
	maxRegister = 0

	operators = {
		"<": operator.lt,
		">": operator.gt,
		"==": operator.eq,
		"!=": operator.ne,
		">=": operator.ge,
		"<=": operator.le,
		"inc": operator.add,
		"dec": operator.sub
	}

	for instructions in data.splitlines():
		register, operation, value, _, conditionRegister, conditionOperation, conditionValue = instructions.split()

		if operators[conditionOperation](registers[conditionRegister],int(conditionValue)):
			registers[register] = operators[operation](registers[register], int(value))

		if operator.gt(max(registers.values()), maxRegister):
			maxRegister = max(registers.values())

	return maxRegister


def main():
	input = read_input("2017_8.txt")
	print("Part 1: " + str(processInstructionsPart1(input)))
	print("Part 2: " + str(processInstructionsPart2(input)))


if __name__ == '__main__':
	main()
