import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

from lib.helper import read_input


def findExitPart1(data):
	maze = list(map(int, data.splitlines()))
	offset = steps = jumps = 0

	while True:
		try:
			jumps = maze[offset]
			maze[offset] += 1
			offset = jumps + offset
			steps += 1
		except IndexError:
			return steps


def findExitPart2(data):
	maze = list(map(int, data.splitlines()))
	offset = steps = jumps = 0

	while True:
		try:
			jumps = maze[offset]

			if jumps >= 3:
				maze[offset] -= 1
			else:
				maze[offset] += 1

			offset = jumps + offset
			steps += 1
		except IndexError:
			return steps


def main():
	input = read_input("2017_5.txt")
	print("Part 1: " + str(findExitPart1(input)))
	print("Part 2: " + str(findExitPart2(input)))


if __name__ == '__main__':
	main()
