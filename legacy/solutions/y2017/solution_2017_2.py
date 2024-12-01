import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + "/.")

from lib.helper import read_input


def checksum_part1(data):
	sumTotal = 0

	for line in data.splitlines():
		values = list(map(int, line.split()))
		sumTotal += max(values) - min(values)

	return sumTotal


def checksum_part2(data):
	sumTotal = 0

	for line in data.splitlines():
		values = list(map(int, line.split()))

		for indexA, _ in enumerate(values):
			for indexB, _ in enumerate(values):
				if (indexA != indexB and values[indexA] % values[indexB] == 0):
					sumTotal += values[indexA] // values[indexB]

	return sumTotal


def main():
	input = read_input("2017_2.txt")
	print("Part 1: " + str(checksum_part1(input)))
	print("Part 2: " + str(checksum_part2(input)))


if __name__ == '__main__':
	main()
