from collections import deque


def spinLockPart1(steps):
	buffer = deque([0])

	for value in range(1, 2018):
		buffer.rotate(-steps)
		buffer.append(value)

	return buffer[0]


def spinLockPart2(steps):
	buffer = deque([0])

	for value in range(1, 50000001):
		buffer.rotate(-steps)
		buffer.append(value)

	return buffer[buffer.index(0) + 1]


def main():
	print("Part 1: " + str(spinLockPart1(304)))
	print("Part 2: " + str(spinLockPart2(304)))


if __name__ == '__main__':
	main()
