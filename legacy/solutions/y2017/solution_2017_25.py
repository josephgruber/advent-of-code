from collections import defaultdict


def checksum(tape):
	return sum(tape.values())


def theHaltingProblem(states, steps):
	tape = defaultdict(float)
	cursor = 0
	state = "A"

	for _ in range(steps):
		value = int(tape[cursor])

		if value == 0 or value == 1:
			tape[cursor] = states[state][value][0]
			cursor += states[state][value][1]
			state = states[state][value][2]

	return checksum(tape)


def main():
	input = {"A": [(1, 1, "B"), (0, -1, "F")],
			"B": [(0, 1, "C"), (0, 1, "D")],
			"C": [(1, -1, "D"), (1, 1, "E")],
			"D": [(0, -1, "E"), (0, -1, "D")],
			"E": [(0, 1, "A"), (1, 1, "C")],
			"F": [(1, -1, "A"), (1, 1, "A")]}
	print("Part 1: " + str(theHaltingProblem(input, 12994925)))


if __name__ == '__main__':
	main()
