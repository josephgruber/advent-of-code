import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from lib.helper import read_input


def captcha_part1(data):
	sumTotal = 0

	for index, _ in enumerate(data):
		if data[index] == data[index-1]:
			sumTotal += int(data[index])

	return sumTotal


def captcha_part2(data):
	halfway = len(data) // 2
	sumTotal = 0

	for index, digit in enumerate(data):
		if index >= halfway:
			pos = index - halfway
		else:
			pos = index + halfway

		if digit == data[pos]:
			sumTotal += int(digit)

	return sumTotal


def main():
	input = read_input("2017_1.txt")
	print("Part 1: " + str(captcha_part1(input)))
	print("Part 2: " + str(captcha_part2(input)))


if __name__ == '__main__':
	main()
