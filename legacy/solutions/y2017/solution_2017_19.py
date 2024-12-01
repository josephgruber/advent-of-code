import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

from lib.helper import read_input


def findStart(row):
	for index, char in enumerate(row):
		if not char.isspace():
			return index


def findDirection(x, y, direction, diagram):
	if direction in ("d", "u"):
		if not diagram[y][x-1].isspace():
			return "l"
		else:
			return "r"
	else:
		if not diagram[y-1][x].isspace():
			return "u"
		else:
			return "d"


def aSeriesOfTubesPart1(diagram):
	diagram = diagram.splitlines()
	directions = {"u": (0, -1), "d": (0, 1), "l": (-1, 0), "r": (1, 0)}
	collectedLetters = []

	x = findStart(diagram[0])
	y = 0
	direction = "d"

	while True:
		x += directions[direction][0]
		y += directions[direction][1]

		char = diagram[y][x]

		if char.isalpha():
			collectedLetters.append(diagram[y][x])
		elif char.isspace():
			return ''.join(collectedLetters)
		elif char == "+":
			direction = findDirection(x, y, direction, diagram)


def aSeriesOfTubesPart2(diagram):
	diagram = diagram.splitlines()
	directions = {"u": (0, -1), "d": (0, 1), "l": (-1, 0), "r": (1, 0)}

	x = findStart(diagram[0])
	y = 0
	direction = "d"
	steps = 0

	while True:
		steps += 1
		x += directions[direction][0]
		y += directions[direction][1]

		char = diagram[y][x]

		if char.isspace():
			return steps
		elif char == "+":
			direction = findDirection(x, y, direction, diagram)


def main():
	input = read_input("2017_19.txt")
	print("Part 1: " + aSeriesOfTubesPart1(input))
	print("Part 2: " + str(aSeriesOfTubesPart2(input)))



if __name__ == '__main__':
	main()
