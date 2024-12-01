import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

from lib.helper import read_input


def spin(instruction, line):
	size = int(instruction[1:])
	return line[-size:] + line[:-size]


def swap(instruction, line, type):
	positions = []

	if type == "x":
		positions.extend(map(int, instruction[1:].split("/")))
	elif type == "p":
		programs = instruction[1:].split("/")
		positions.append(line.index(programs[0]))
		positions.append(line.index(programs[1]))

	tempA = line[positions[0]]
	line[positions[0]] = line[positions[1]]
	line[positions[1]] = tempA

	return line


def permutationPromenadePart1(line, moves):
	line = list(line)

	for move in moves.split(","):
		if move[:1] == "s":
			line = spin(move, line)
		elif move[:1] == "x":
			line = swap(move, line, "x")
		elif move[:1] == "p":
			line = swap(move, line, "p")

	return ''.join(line)


def permutationPromenadePart2(line, moves):
	line = list(line)

	# Determined cycle count to be 24
	for _ in range(999999984, 1000000000):
		for move in moves.split(","):
			if move[:1] == "s":
				line = spin(move, line)
			elif move[:1] == "x":
				line = swap(move, line, "x")
			elif move[:1] == "p":
				line = swap(move, line, "p")

	return ''.join(line)


def main():
	input = read_input("2017_16.txt")
	print("Part 1: " + permutationPromenadePart1("abcdefghijklmnop", input))
	print("Part 2: " + permutationPromenadePart2("abcdefghijklmnop", input))


if __name__ == '__main__':
	main()
